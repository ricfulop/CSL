#!/usr/bin/env python3
"""
Continue scraping with improved configuration
Focuses on sites that failed or need Selenium
"""

import os
import sys
import time
from pathlib import Path
from doc_scraper import DocumentationScraper
from search_docs import DocumentationSearcher

def main():
    print("=" * 60)
    print("Continuing Documentation Scraping")
    print("=" * 60)
    print("\nThis will scrape the sites that had issues:")
    print("- FreeCAD Wiki (with Selenium for JavaScript)")
    print("- FreeCAD Source Documentation")
    print("- KiCad (fixed URL)")
    print("- Rhino (better patterns)")
    print("- Additional open source CAD tools")
    print("-" * 60)
    
    response = input("\nProceed? (y/n): ")
    if response.lower() != 'y':
        print("Cancelled.")
        return
    
    # Check if Chrome/Chromium is available for Selenium
    print("\n🔍 Checking Selenium requirements...")
    try:
        from selenium import webdriver
        from selenium.webdriver.chrome.options import Options
        
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        
        # Test if Chrome driver works
        try:
            driver = webdriver.Chrome(options=options)
            driver.quit()
            print("✅ Selenium Chrome driver is working")
        except Exception as e:
            print(f"⚠️ Selenium not available: {e}")
            print("Installing Chrome driver...")
            
            # Try to install via webdriver-manager
            from webdriver_manager.chrome import ChromeDriverManager
            from selenium.webdriver.chrome.service import Service
            
            service = Service(ChromeDriverManager().install())
            driver = webdriver.Chrome(service=service, options=options)
            driver.quit()
            print("✅ Chrome driver installed successfully")
            
    except ImportError:
        print("⚠️ Selenium not installed, skipping JavaScript sites")
    except Exception as e:
        print(f"⚠️ Selenium setup failed: {e}")
        print("Continuing without JavaScript support...")
    
    # Initialize scraper with improved config
    print("\n🚀 Initializing scraper with improved configuration...")
    scraper = DocumentationScraper('improved_config.yaml')
    
    # Sites to scrape (prioritized)
    sites_to_scrape = [
        # Try FreeCAD with Selenium
        ('freecad_wiki', 'FreeCAD Wiki (with JavaScript handling)'),
        ('freecad_source', 'FreeCAD Source Documentation'),
        ('freecad_api', 'FreeCAD Python API'),
        
        # Retry KiCad and Rhino with better config
        ('kicad', 'KiCad Python Documentation'),
        ('kicad_main', 'KiCad Main Documentation'),
        ('rhino', 'Rhino Developer Documentation'),
        ('grasshopper', 'Grasshopper API'),
        
        # Additional open source tools
        ('openscad', 'OpenSCAD Documentation'),
        ('openjscad', 'OpenJSCAD Documentation'),
        ('solvespace', 'SolveSpace Documentation'),
    ]
    
    successful = []
    failed = []
    
    for site_key, site_name in sites_to_scrape:
        print(f"\n📥 Scraping {site_name}...")
        print("=" * 60)
        
        try:
            site_config = scraper.config['sites'].get(site_key, {})
            if not site_config.get('enabled', False):
                print(f"⏭️  Skipped (disabled in config)")
                continue
            
            # Check if we need Selenium and if it's available
            if site_config.get('use_selenium', False) and not scraper._driver:
                print(f"⚠️ Skipping {site_name} - requires Selenium which is not available")
                failed.append(site_name)
                continue
            
            scraper.scrape_site(
                site_key,
                site_config['start_url'],
                max_depth=site_config.get('max_depth', 3),
                max_pages=site_config.get('max_pages', 500)
            )
            
            print(f"✅ Completed {site_name}")
            successful.append(site_name)
            
        except KeyboardInterrupt:
            print("\n⚠️ Scraping interrupted by user")
            break
        except Exception as e:
            print(f"❌ Error scraping {site_name}: {e}")
            failed.append(site_name)
            continue
        
        # Brief pause between sites
        time.sleep(2)
    
    # Rebuild search index
    print("\n" + "=" * 60)
    print("📊 Rebuilding search index...")
    
    searcher = DocumentationSearcher('documentation_archive')
    searcher.build_index(force_rebuild=True)
    
    # Show final statistics
    stats = searcher.get_stats()
    print("\n✅ Scraping Session Complete!")
    print("-" * 60)
    print(f"📄 Total documents: {stats['total_documents']}")
    print(f"💾 Index size: {stats['index_size'] / 1024 / 1024:.2f} MB")
    print(f"🌐 Sites indexed: {len(stats['sites'])}")
    
    if successful:
        print(f"\n✅ Successfully scraped ({len(successful)}):")
        for site in successful:
            print(f"   - {site}")
    
    if failed:
        print(f"\n❌ Failed to scrape ({len(failed)}):")
        for site in failed:
            print(f"   - {site}")
    
    print("\n🔍 Search your documentation:")
    print("   python3 search_docs.py --interactive")
    print("=" * 60)

if __name__ == '__main__':
    main()
