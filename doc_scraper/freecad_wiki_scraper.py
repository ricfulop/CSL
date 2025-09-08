#!/usr/bin/env python3
"""
Specialized FreeCAD Wiki Scraper with Selenium
Handles Anubis anti-bot protection
"""

import os
import time
import json
from pathlib import Path
from typing import List, Set
from urllib.parse import urljoin, urlparse

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from bs4 import BeautifulSoup
import html2text
from tqdm import tqdm

class FreeCADWikiScraper:
    """Specialized scraper for FreeCAD Wiki with Anubis handling"""
    
    def __init__(self, output_dir: str = "documentation_archive/freecad_wiki"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
        self.visited_urls: Set[str] = set()
        self.failed_urls: Set[str] = set()
        
        # HTML to text converter
        self.html2text = html2text.HTML2Text()
        self.html2text.ignore_links = False
        self.html2text.ignore_images = False
        
        # Important FreeCAD Wiki pages to scrape
        self.priority_pages = [
            "https://wiki.freecad.org/Main_Page",
            "https://wiki.freecad.org/Power_users_hub",
            "https://wiki.freecad.org/Python",
            "https://wiki.freecad.org/Introduction_to_Python",
            "https://wiki.freecad.org/Python_scripting_tutorial",
            "https://wiki.freecad.org/FreeCAD_Scripting_Basics",
            "https://wiki.freecad.org/Topological_data_scripting",
            "https://wiki.freecad.org/Mesh_Scripting",
            "https://wiki.freecad.org/Part_scripting",
            "https://wiki.freecad.org/Scripted_objects",
            "https://wiki.freecad.org/Viewprovider",
            "https://wiki.freecad.org/Pivy",
            "https://wiki.freecad.org/PySide",
            "https://wiki.freecad.org/Macros",
            "https://wiki.freecad.org/Gui_Command",
            "https://wiki.freecad.org/Workbench_creation",
            "https://wiki.freecad.org/Debugging",
            "https://wiki.freecad.org/Code_snippets",
            "https://wiki.freecad.org/Line_drawing_function",
            "https://wiki.freecad.org/Dialog_creation",
            "https://wiki.freecad.org/Embedding_FreeCAD",
            "https://wiki.freecad.org/FreeCAD_vector_math_library",
            # Workbench-specific scripting
            "https://wiki.freecad.org/Draft_API",
            "https://wiki.freecad.org/Arch_API", 
            "https://wiki.freecad.org/Part_API",
            "https://wiki.freecad.org/PartDesign_API",
            "https://wiki.freecad.org/Sketcher_API",
            "https://wiki.freecad.org/TechDraw_API",
            # Module documentation
            "https://wiki.freecad.org/Builtin_modules",
            "https://wiki.freecad.org/Units",
            "https://wiki.freecad.org/Quantity",
            "https://wiki.freecad.org/Placement",
            "https://wiki.freecad.org/Scenegraph",
            "https://wiki.freecad.org/Coin",
            "https://wiki.freecad.org/Console_API",
            "https://wiki.freecad.org/FreeCADGui_API",
            # Property system
            "https://wiki.freecad.org/Property",
            "https://wiki.freecad.org/PropertyLink",
            "https://wiki.freecad.org/Expressions",
            # Examples and tutorials
            "https://wiki.freecad.org/Tutorials",
            "https://wiki.freecad.org/Python_Development_Environment",
            "https://wiki.freecad.org/Debugging#Python_Debugging",
            "https://wiki.freecad.org/Profiling",
            # Object creation
            "https://wiki.freecad.org/Creating_a_simple_part_with_Part_WB",
            "https://wiki.freecad.org/Creating_a_simple_part_with_Draft_and_Part_WB",
            "https://wiki.freecad.org/Creating_a_simple_part_with_PartDesign",
            "https://wiki.freecad.org/Scripts",
            "https://wiki.freecad.org/Macros_recipes",
        ]
        
        self.driver = None
    
    def init_driver(self):
        """Initialize Selenium driver with proper options"""
        if self.driver:
            return
            
        options = Options()
        # Run in headless mode for speed
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--disable-gpu')
        options.add_argument('--disable-web-security')
        options.add_argument('--disable-features=VizDisplayCompositor')
        # Important: Set a real user agent
        options.add_argument('--user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36')
        
        # Use webdriver-manager to handle driver
        try:
            from webdriver_manager.chrome import ChromeDriverManager
            service = Service(ChromeDriverManager().install())
            self.driver = webdriver.Chrome(service=service, options=options)
            # Set page load timeout
            self.driver.set_page_load_timeout(30)
            print("✅ Chrome driver initialized successfully")
        except Exception as e:
            print(f"❌ Failed to initialize Chrome driver: {e}")
            raise
    
    def wait_for_anubis(self, timeout: int = 30) -> bool:
        """Wait for Anubis challenge to complete"""
        try:
            # Check if Anubis is present
            if "anubis" in self.driver.page_source.lower():
                print("⏳ Anubis protection detected, waiting for challenge...")
                
                # Wait for the actual content to load (Anubis to disappear)
                wait = WebDriverWait(self.driver, timeout)
                
                # Wait for wiki content to appear
                wait.until(
                    EC.presence_of_element_located((By.ID, "content"))
                )
                
                # Additional wait to ensure full load
                time.sleep(2)
                
                # Check if we're still on Anubis page
                if "Making sure you're not a bot" in self.driver.page_source:
                    print("⚠️ Anubis challenge still active, waiting longer...")
                    time.sleep(5)
                    
                    # Try to wait for specific wiki elements
                    wait.until(
                        EC.presence_of_element_located((By.CLASS_NAME, "mw-parser-output"))
                    )
                
                print("✅ Anubis challenge passed")
                return True
                
        except TimeoutException:
            print("⚠️ Timeout waiting for Anubis challenge")
            return False
        
        return True
    
    def scrape_page(self, url: str) -> tuple[str, List[str]]:
        """Scrape a single Wiki page"""
        if url in self.visited_urls:
            return None, []
        
        self.visited_urls.add(url)
        
        try:
            # Navigate to page
            self.driver.get(url)
            
            # Handle Anubis protection
            if not self.wait_for_anubis():
                self.failed_urls.add(url)
                return None, []
            
            # Get page source after JavaScript execution
            soup = BeautifulSoup(self.driver.page_source, 'html.parser')
            
            # Remove unwanted elements
            for element in soup.select('#mw-navigation, #footer, .printfooter, .catlinks, .mw-editsection'):
                element.decompose()
            
            # Extract main content
            content = soup.select_one('#mw-content-text, #content, .mw-parser-output')
            
            if not content:
                print(f"⚠️ No content found for {url}")
                return None, []
            
            # Convert to markdown
            text_content = self.html2text.handle(str(content))
            
            # Extract links (only FreeCAD wiki links)
            links = []
            for link in soup.find_all('a', href=True):
                href = link['href']
                if href.startswith('/'):
                    href = f"https://wiki.freecad.org{href}"
                elif not href.startswith('http'):
                    href = urljoin(url, href)
                
                # Only follow FreeCAD wiki links
                if 'wiki.freecad.org' in href and '#' not in href:
                    # Skip special pages, non-content, and non-English pages
                    skip_patterns = ['Special:', 'Talk:', 'action=', 'oldid=', 'File:', 'User:',
                                   '/de', '/es', '/fr', '/it', '/ja', '/pl', '/pt', '/ru', '/zh',
                                   '/cs', '/tr', '/ko', '/sv', '/uk', '/ro', '/hr', '/id']
                    if not any(skip in href for skip in skip_patterns):
                        links.append(href)
            
            return text_content, links
            
        except Exception as e:
            print(f"❌ Error scraping {url}: {e}")
            self.failed_urls.add(url)
            return None, []
    
    def save_content(self, url: str, content: str):
        """Save scraped content to file"""
        parsed = urlparse(url)
        path = parsed.path.strip('/') or 'index'
        
        # Clean filename
        filename = path.replace('/', '_') + '.md'
        file_path = self.output_dir / filename
        
        # Save with metadata
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(f"---\n")
            f.write(f"url: {url}\n")
            f.write(f"title: {path.replace('_', ' ')}\n")
            f.write(f"scraped_at: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"---\n\n")
            f.write(content)
        
        return file_path
    
    def scrape_wiki(self, max_pages: int = 500):
        """Scrape FreeCAD Wiki with priority pages first"""
        self.init_driver()
        
        print(f"📚 Starting FreeCAD Wiki scrape (max {max_pages} pages)")
        print(f"📍 Priority pages: {len(self.priority_pages)}")
        
        # Start with priority pages
        to_visit = self.priority_pages.copy()
        pages_scraped = 0
        
        try:
            with tqdm(total=max_pages, desc="Scraping FreeCAD Wiki") as pbar:
                while to_visit and pages_scraped < max_pages:
                    url = to_visit.pop(0)
                    
                    if url in self.visited_urls:
                        continue
                    
                    content, links = self.scrape_page(url)
                    
                    if content:
                        self.save_content(url, content)
                        pages_scraped += 1
                        pbar.update(1)
                        
                        # Add new links to queue (after priority pages)
                        for link in links:
                            if link not in self.visited_urls and link not in to_visit:
                                to_visit.append(link)
                        
                        # Rate limiting
                        time.sleep(1)
                    
                    # Save progress periodically
                    if pages_scraped % 10 == 0:
                        self.save_progress()
            
            print(f"\n✅ Scraped {pages_scraped} pages successfully")
            
            if self.failed_urls:
                print(f"⚠️ Failed to scrape {len(self.failed_urls)} pages:")
                for url in list(self.failed_urls)[:5]:
                    print(f"  - {url}")
                    
        finally:
            if self.driver:
                self.driver.quit()
            self.save_progress()
    
    def save_progress(self):
        """Save scraping progress to file"""
        progress_file = self.output_dir / "scrape_progress.json"
        with open(progress_file, 'w') as f:
            json.dump({
                'visited': list(self.visited_urls),
                'failed': list(self.failed_urls),
                'scraped_at': time.strftime('%Y-%m-%d %H:%M:%S')
            }, f, indent=2)

def main():
    """Main entry point"""
    import argparse
    
    parser = argparse.ArgumentParser(description='Scrape FreeCAD Wiki documentation')
    parser.add_argument('--max-pages', type=int, default=200, help='Maximum pages to scrape')
    parser.add_argument('--output', default='documentation_archive/freecad_wiki', help='Output directory')
    
    args = parser.parse_args()
    
    scraper = FreeCADWikiScraper(args.output)
    scraper.scrape_wiki(args.max_pages)

if __name__ == '__main__':
    main()
