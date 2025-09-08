#!/usr/bin/env python3
"""
Quick start script to scrape essential CAD documentation
Focuses on free/public documentation that doesn't require authentication
"""

import os
import sys
from pathlib import Path
import yaml
import time
from doc_scraper import DocumentationScraper
from search_docs import DocumentationSearcher

def create_minimal_config():
    """Create a minimal configuration for public documentation"""
    config = {
        'output_dir': 'documentation_archive',
        'rate_limit': 1.0,
        'authentication': {},
        'sites': {
            # Free/public documentation
            'freecad': {
                'enabled': True,
                'start_url': 'https://wiki.freecad.org/Api',
                'max_depth': 3,
                'max_pages': 500,
                'url_patterns': ['wiki.freecad.org']
            },
            'blender': {
                'enabled': True,
                'start_url': 'https://docs.blender.org/api/current/',
                'max_depth': 3,
                'max_pages': 500,
                'url_patterns': ['docs.blender.org/api']
            },
            'onshape_featurescript': {
                'enabled': True,
                'start_url': 'https://cad.onshape.com/FsDoc/',
                'max_depth': 3,
                'max_pages': 500,
                'url_patterns': ['cad.onshape.com/FsDoc']
            },
            'kicad': {
                'enabled': True,
                'start_url': 'https://docs.kicad.org/doxygen-python/',
                'max_depth': 3,
                'max_pages': 300,
                'url_patterns': ['docs.kicad.org']
            },
            'rhino': {
                'enabled': True,
                'start_url': 'https://developer.rhino3d.com/api/RhinoCommon/',
                'max_depth': 3,
                'max_pages': 1000,
                'url_patterns': ['developer.rhino3d.com']
            }
        }
    }
    
    # Save config
    config_file = Path('quick_start_config.yaml')
    with open(config_file, 'w') as f:
        yaml.dump(config, f, default_flow_style=False)
    
    return config_file

def main():
    """Run quick start scraping"""
    print("=" * 60)
    print("Documentation Scraper - Quick Start")
    print("=" * 60)
    print("\nThis will scrape publicly available documentation from:")
    print("- FreeCAD Wiki & API")
    print("- Blender Python API")
    print("- Onshape FeatureScript")
    print("- KiCad Python API")
    print("- Rhino/Grasshopper API")
    print("\nNo authentication required for these sites!")
    print("-" * 60)
    
    # Check if user wants to proceed
    response = input("\nProceed with scraping? (y/n): ")
    if response.lower() != 'y':
        print("Cancelled.")
        return
    
    # Create config
    print("\n📝 Creating configuration...")
    config_file = create_minimal_config()
    
    # Initialize scraper
    print("🚀 Initializing scraper...")
    scraper = DocumentationScraper(str(config_file))
    
    # Scrape each site
    sites_to_scrape = ['freecad', 'blender', 'onshape_featurescript', 'kicad', 'rhino']
    
    for site in sites_to_scrape:
        print(f"\n📥 Scraping {site}...")
        print("=" * 60)
        
        try:
            site_config = scraper.config['sites'][site]
            if site_config.get('enabled', True):
                scraper.scrape_site(
                    site,
                    site_config['start_url'],
                    max_depth=site_config.get('max_depth', 3),
                    max_pages=site_config.get('max_pages', 500)
                )
                print(f"✅ Completed {site}")
            else:
                print(f"⏭️  Skipped {site} (disabled)")
        except Exception as e:
            print(f"❌ Error scraping {site}: {e}")
            continue
        
        # Brief pause between sites
        time.sleep(2)
    
    print("\n" + "=" * 60)
    print("📊 Building search index...")
    
    # Build search index
    searcher = DocumentationSearcher('documentation_archive')
    searcher.build_index(force_rebuild=True)
    
    # Show statistics
    stats = searcher.get_stats()
    print("\n✅ Scraping Complete!")
    print("-" * 60)
    print(f"📄 Total documents: {stats['total_documents']}")
    print(f"💾 Index size: {stats['index_size'] / 1024 / 1024:.2f} MB")
    print(f"🌐 Sites indexed: {len(stats['sites'])}")
    
    print("\n🔍 You can now search the documentation:")
    print("   python search_docs.py --interactive")
    print("   python search_docs.py 'your search query'")
    
    print("\n📁 Documentation saved to: documentation_archive/")
    print("=" * 60)

if __name__ == '__main__':
    main()
