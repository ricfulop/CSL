#!/usr/bin/env python3
"""
Comprehensive Documentation Scraper for Engineering Software APIs
Supports authentication, rate limiting, and multiple documentation formats
"""

import os
import re
import json
import time
import hashlib
import logging
import argparse
from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple
from urllib.parse import urljoin, urlparse, parse_qs
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed
import pickle

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import markdown
import html2text
from tqdm import tqdm
import yaml

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class DocumentationScraper:
    """Main documentation scraper class with authentication and rate limiting"""
    
    def __init__(self, config_path: str = "scraper_config.yaml"):
        """Initialize scraper with configuration"""
        self.config = self._load_config(config_path)
        self.base_dir = Path(self.config.get('output_dir', 'documentation_archive'))
        self.base_dir.mkdir(parents=True, exist_ok=True)
        
        # Session management
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
        })
        
        # Rate limiting
        self.rate_limit = self.config.get('rate_limit', 1.0)  # seconds between requests
        self.last_request_time = {}
        
        # Cache for visited URLs
        self.visited_urls: Set[str] = set()
        self.url_queue: List[Tuple[str, int]] = []  # (url, depth)
        
        # Selenium driver (lazy loaded)
        self._driver = None
        
        # HTML to text converter
        self.html2text = html2text.HTML2Text()
        self.html2text.ignore_links = False
        self.html2text.ignore_images = False
        
        # Index for searchability
        self.index = {}
        self.index_file = self.base_dir / "documentation_index.json"
        
    def _load_config(self, config_path: str) -> Dict:
        """Load configuration from YAML file"""
        config_file = Path(config_path)
        if config_file.exists():
            with open(config_file, 'r') as f:
                return yaml.safe_load(f) or {}
        return {}
    
    @property
    def driver(self):
        """Lazy load Selenium driver for JavaScript-heavy sites"""
        if self._driver is None:
            options = Options()
            options.add_argument('--headless')
            options.add_argument('--no-sandbox')
            options.add_argument('--disable-dev-shm-usage')
            options.add_argument('--disable-gpu')
            options.add_experimental_option('excludeSwitches', ['enable-logging'])
            
            try:
                self._driver = webdriver.Chrome(options=options)
                logger.info("Selenium Chrome driver initialized")
            except Exception as e:
                logger.warning(f"Failed to initialize Chrome driver: {e}")
                self._driver = None
        
        return self._driver
    
    def authenticate(self, site_name: str) -> bool:
        """Authenticate to a specific documentation site"""
        auth_config = self.config.get('authentication', {}).get(site_name, {})
        
        if not auth_config:
            logger.info(f"No authentication configured for {site_name}")
            return True
        
        auth_type = auth_config.get('type', 'basic')
        
        if auth_type == 'basic':
            self.session.auth = (auth_config['username'], auth_config['password'])
            logger.info(f"Basic authentication configured for {site_name}")
            
        elif auth_type == 'oauth':
            # Handle OAuth flow
            token = auth_config.get('token')
            if token:
                self.session.headers['Authorization'] = f"Bearer {token}"
                logger.info(f"OAuth token configured for {site_name}")
            
        elif auth_type == 'form':
            # Handle form-based login
            login_url = auth_config.get('login_url')
            username = auth_config.get('username')
            password = auth_config.get('password')
            
            if login_url and username and password:
                self._form_login(login_url, username, password, auth_config)
                
        elif auth_type == 'selenium':
            # Use Selenium for complex JavaScript authentication
            if self.driver:
                self._selenium_login(auth_config)
        
        return True
    
    def _form_login(self, login_url: str, username: str, password: str, config: Dict):
        """Handle form-based authentication"""
        try:
            # Get login page
            resp = self.session.get(login_url)
            soup = BeautifulSoup(resp.content, 'html.parser')
            
            # Find form and extract fields
            form = soup.find('form')
            if not form:
                logger.warning("No form found on login page")
                return
            
            # Build form data
            form_data = {
                config.get('username_field', 'username'): username,
                config.get('password_field', 'password'): password
            }
            
            # Add any hidden fields
            for hidden in form.find_all('input', type='hidden'):
                if hidden.get('name'):
                    form_data[hidden['name']] = hidden.get('value', '')
            
            # Submit login
            action = form.get('action', login_url)
            if not action.startswith('http'):
                action = urljoin(login_url, action)
            
            resp = self.session.post(action, data=form_data)
            
            if resp.status_code == 200:
                logger.info(f"Successfully logged in via form")
            else:
                logger.warning(f"Form login returned status {resp.status_code}")
                
        except Exception as e:
            logger.error(f"Form login failed: {e}")
    
    def _selenium_login(self, config: Dict):
        """Handle complex JavaScript-based authentication using Selenium"""
        try:
            login_url = config.get('login_url')
            username = config.get('username')
            password = config.get('password')
            
            self.driver.get(login_url)
            
            # Wait for login form
            wait = WebDriverWait(self.driver, 10)
            
            # Find and fill username
            username_field = wait.until(
                EC.presence_of_element_located((By.NAME, config.get('username_field', 'username')))
            )
            username_field.send_keys(username)
            
            # Find and fill password
            password_field = self.driver.find_element(By.NAME, config.get('password_field', 'password'))
            password_field.send_keys(password)
            
            # Submit form
            submit_button = self.driver.find_element(By.CSS_SELECTOR, config.get('submit_selector', 'button[type="submit"]'))
            submit_button.click()
            
            # Wait for login to complete
            time.sleep(3)
            
            # Transfer cookies to requests session
            for cookie in self.driver.get_cookies():
                self.session.cookies.set(cookie['name'], cookie['value'])
            
            logger.info("Successfully logged in via Selenium")
            
        except Exception as e:
            logger.error(f"Selenium login failed: {e}")
    
    def scrape_site(self, site_name: str, start_url: str, max_depth: int = 5, max_pages: int = 10000):
        """Scrape documentation from a specific site"""
        logger.info(f"Starting scrape for {site_name}: {start_url}")
        
        # Create site directory
        site_dir = self.base_dir / site_name
        site_dir.mkdir(parents=True, exist_ok=True)
        
        # Authenticate if needed
        self.authenticate(site_name)
        
        # Initialize queue
        self.url_queue = [(start_url, 0)]
        self.visited_urls = set()
        
        # Site-specific configuration
        site_config = self.config.get('sites', {}).get(site_name, {})
        url_patterns = site_config.get('url_patterns', [])
        exclude_patterns = site_config.get('exclude_patterns', [])
        
        pages_scraped = 0
        
        with tqdm(total=max_pages, desc=f"Scraping {site_name}") as pbar:
            while self.url_queue and pages_scraped < max_pages:
                url, depth = self.url_queue.pop(0)
                
                # Skip if already visited or exceeds depth
                if url in self.visited_urls or depth > max_depth:
                    continue
                
                # Check URL patterns
                if url_patterns and not any(re.search(pattern, url) for pattern in url_patterns):
                    continue
                
                if exclude_patterns and any(re.search(pattern, url) for pattern in exclude_patterns):
                    continue
                
                # Rate limiting
                self._rate_limit(url)
                
                # Scrape page
                try:
                    content, links = self._scrape_page(url, site_name)
                    
                    if content:
                        # Save content
                        file_path = self._save_content(url, content, site_dir)
                        
                        # Update index
                        self._update_index(site_name, url, file_path, content)
                        
                        # Add new links to queue
                        for link in links:
                            if link not in self.visited_urls:
                                self.url_queue.append((link, depth + 1))
                        
                        self.visited_urls.add(url)
                        pages_scraped += 1
                        pbar.update(1)
                        
                except Exception as e:
                    logger.error(f"Error scraping {url}: {e}")
                    continue
        
        logger.info(f"Completed scraping {site_name}: {pages_scraped} pages")
        
        # Save index
        self._save_index()
    
    def _rate_limit(self, url: str):
        """Implement rate limiting per domain"""
        domain = urlparse(url).netloc
        
        if domain in self.last_request_time:
            elapsed = time.time() - self.last_request_time[domain]
            if elapsed < self.rate_limit:
                time.sleep(self.rate_limit - elapsed)
        
        self.last_request_time[domain] = time.time()
    
    def _scrape_page(self, url: str, site_name: str) -> Tuple[str, List[str]]:
        """Scrape a single page and extract content and links"""
        # Check if we need Selenium for this site
        site_config = self.config.get('sites', {}).get(site_name, {})
        use_selenium = site_config.get('use_selenium', False)
        
        if use_selenium and self.driver:
            return self._scrape_with_selenium(url)
        else:
            return self._scrape_with_requests(url)
    
    def _scrape_with_requests(self, url: str) -> Tuple[str, List[str]]:
        """Scrape page using requests library"""
        try:
            resp = self.session.get(url, timeout=30)
            resp.raise_for_status()
            
            # Parse content
            soup = BeautifulSoup(resp.content, 'html.parser')
            
            # Extract main content (try common content containers)
            content_selectors = [
                'main', 'article', '.content', '#content', 
                '.documentation', '.doc-content', '.markdown-body'
            ]
            
            content = None
            for selector in content_selectors:
                element = soup.select_one(selector)
                if element:
                    content = element
                    break
            
            if not content:
                content = soup.body or soup
            
            # Convert to markdown
            text_content = self.html2text.handle(str(content))
            
            # Extract links
            links = []
            for link in soup.find_all('a', href=True):
                href = link['href']
                absolute_url = urljoin(url, href)
                
                # Only follow documentation links
                if self._is_documentation_link(absolute_url):
                    links.append(absolute_url)
            
            return text_content, links
            
        except Exception as e:
            logger.error(f"Failed to scrape {url}: {e}")
            return None, []
    
    def _scrape_with_selenium(self, url: str) -> Tuple[str, List[str]]:
        """Scrape JavaScript-heavy page using Selenium"""
        try:
            self.driver.get(url)
            
            # Wait for content to load
            time.sleep(2)
            
            # Get page source
            soup = BeautifulSoup(self.driver.page_source, 'html.parser')
            
            # Extract content (similar to requests method)
            content_selectors = [
                'main', 'article', '.content', '#content',
                '.documentation', '.doc-content', '.markdown-body'
            ]
            
            content = None
            for selector in content_selectors:
                element = soup.select_one(selector)
                if element:
                    content = element
                    break
            
            if not content:
                content = soup.body or soup
            
            # Convert to markdown
            text_content = self.html2text.handle(str(content))
            
            # Extract links
            links = []
            for link in soup.find_all('a', href=True):
                href = link['href']
                absolute_url = urljoin(url, href)
                
                if self._is_documentation_link(absolute_url):
                    links.append(absolute_url)
            
            return text_content, links
            
        except Exception as e:
            logger.error(f"Selenium scrape failed for {url}: {e}")
            return None, []
    
    def _is_documentation_link(self, url: str) -> bool:
        """Check if URL is likely a documentation link"""
        # Skip external links
        parsed = urlparse(url)
        
        # Skip non-HTTP(S) links
        if parsed.scheme and parsed.scheme not in ['http', 'https']:
            return False
        
        # Skip common non-documentation paths
        skip_patterns = [
            r'/login', r'/logout', r'/register', r'/download',
            r'/pricing', r'/blog', r'/news', r'/forum',
            r'\.(pdf|zip|exe|dmg|pkg|deb|rpm|tar|gz)$'
        ]
        
        for pattern in skip_patterns:
            if re.search(pattern, url, re.I):
                return False
        
        return True
    
    def _save_content(self, url: str, content: str, site_dir: Path) -> Path:
        """Save scraped content to file"""
        # Generate filename from URL
        parsed = urlparse(url)
        path = parsed.path.strip('/') or 'index'
        path = re.sub(r'[^\w\-/]', '_', path)
        
        # Create subdirectories
        file_path = site_dir / f"{path}.md"
        file_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Save content with metadata
        metadata = {
            'url': url,
            'scraped_at': datetime.now().isoformat(),
            'title': self._extract_title(content)
        }
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(f"---\n")
            for key, value in metadata.items():
                f.write(f"{key}: {value}\n")
            f.write(f"---\n\n")
            f.write(content)
        
        return file_path
    
    def _extract_title(self, content: str) -> str:
        """Extract title from markdown content"""
        lines = content.split('\n')
        for line in lines[:10]:  # Check first 10 lines
            if line.startswith('# '):
                return line[2:].strip()
        return "Untitled"
    
    def _update_index(self, site_name: str, url: str, file_path: Path, content: str):
        """Update search index with page content"""
        # Create searchable entry
        entry = {
            'site': site_name,
            'url': url,
            'file': str(file_path.relative_to(self.base_dir)),
            'title': self._extract_title(content),
            'content_preview': content[:500],  # First 500 chars
            'word_count': len(content.split()),
            'indexed_at': datetime.now().isoformat()
        }
        
        # Add to index
        if site_name not in self.index:
            self.index[site_name] = {}
        
        self.index[site_name][url] = entry
    
    def _save_index(self):
        """Save search index to file"""
        with open(self.index_file, 'w', encoding='utf-8') as f:
            json.dump(self.index, f, indent=2)
        
        logger.info(f"Saved index with {sum(len(s) for s in self.index.values())} entries")
    
    def search(self, query: str, site: Optional[str] = None) -> List[Dict]:
        """Search the indexed documentation"""
        results = []
        query_lower = query.lower()
        
        # Load index if not in memory
        if not self.index and self.index_file.exists():
            with open(self.index_file, 'r') as f:
                self.index = json.load(f)
        
        # Search across sites
        for site_name, pages in self.index.items():
            if site and site != site_name:
                continue
            
            for url, entry in pages.items():
                # Simple text search (can be improved with proper search engine)
                if (query_lower in entry['title'].lower() or 
                    query_lower in entry['content_preview'].lower()):
                    results.append(entry)
        
        return results
    
    def scrape_all(self):
        """Scrape all configured documentation sites"""
        sites = self.config.get('sites', {})
        
        for site_name, site_config in sites.items():
            if site_config.get('enabled', True):
                start_url = site_config.get('start_url')
                if start_url:
                    try:
                        self.scrape_site(
                            site_name,
                            start_url,
                            max_depth=site_config.get('max_depth', 5),
                            max_pages=site_config.get('max_pages', 10000)
                        )
                    except Exception as e:
                        logger.error(f"Failed to scrape {site_name}: {e}")
        
        # Cleanup
        if self._driver:
            self._driver.quit()

def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(description='Scrape engineering software documentation')
    parser.add_argument('--config', default='scraper_config.yaml', help='Configuration file')
    parser.add_argument('--site', help='Specific site to scrape')
    parser.add_argument('--search', help='Search query')
    parser.add_argument('--all', action='store_true', help='Scrape all configured sites')
    
    args = parser.parse_args()
    
    scraper = DocumentationScraper(args.config)
    
    if args.search:
        # Search mode
        results = scraper.search(args.search, args.site)
        print(f"\nFound {len(results)} results for '{args.search}':\n")
        for result in results[:10]:
            print(f"📄 {result['title']}")
            print(f"   Site: {result['site']}")
            print(f"   URL: {result['url']}")
            print(f"   File: {result['file']}")
            print()
    
    elif args.all:
        # Scrape all sites
        scraper.scrape_all()
    
    elif args.site:
        # Scrape specific site
        site_config = scraper.config.get('sites', {}).get(args.site, {})
        start_url = site_config.get('start_url')
        if start_url:
            scraper.scrape_site(args.site, start_url)
        else:
            print(f"No configuration found for site: {args.site}")
    
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
