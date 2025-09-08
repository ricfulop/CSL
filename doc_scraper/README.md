# Engineering Software Documentation Scraper

A comprehensive scraper for downloading and indexing API documentation from major CAD, EDA, BIM, and design software packages. This tool creates a local, searchable archive of documentation that AI agents can reference for faster coding.

## 🎯 Features

- **Multi-site Support**: Scrapes documentation from 20+ engineering software platforms
- **Authentication Handling**: Supports OAuth, form-based login, and Selenium for complex JS auth
- **Smart Content Extraction**: Site-specific parsers for optimal content extraction
- **Full-Text Search**: Fast, indexed search across all documentation
- **Rate Limiting**: Respectful scraping with configurable delays
- **Incremental Updates**: Resume interrupted scrapes, skip already downloaded content
- **Multiple Formats**: Handles HTML, Markdown, and extracts from PDFs

## 📦 Installation

```bash
# Clone or copy the doc_scraper directory
cd doc_scraper

# Install dependencies
pip install -r requirements.txt

# For Selenium support (JavaScript-heavy sites), install Chrome driver
pip install webdriver-manager

# On macOS, you may need:
brew install --cask chromedriver
```

## ⚙️ Configuration

1. **Copy and edit the configuration file:**

```bash
cp scraper_config.yaml my_config.yaml
```

2. **Add your credentials** (keep this file secure!):

```yaml
authentication:
  autodesk:
    type: oauth
    token: "YOUR_AUTODESK_TOKEN"  # Get from Autodesk App Store
  
  solidworks:
    type: form
    username: "your.email@example.com"
    password: "your_password"
```

3. **Configure sites to scrape:**

```yaml
sites:
  fusion360:
    enabled: true              # Enable/disable this site
    max_depth: 5               # How deep to follow links
    max_pages: 5000           # Maximum pages to scrape
    use_selenium: false       # Use Selenium for JS-heavy pages
```

## 🚀 Quick Start

### 1. Scrape All Configured Sites

```bash
python doc_scraper.py --all --config my_config.yaml
```

### 2. Scrape a Specific Site

```bash
python doc_scraper.py --site fusion360 --config my_config.yaml
```

### 3. Build Search Index

```bash
python search_docs.py --build
```

### 4. Interactive Search

```bash
python search_docs.py --interactive

# Or search directly from command line
python search_docs.py "sketch constraint api"
python search_docs.py "fusion extrude" --site fusion360
```

## 📊 Supported Documentation Sites

### CAD Systems
- ✅ **Fusion 360** - Full API and help documentation
- ✅ **Inventor** - Automation API
- ✅ **SolidWorks** - Complete API reference (requires login)
- ⚠️ **Siemens NX** - NX Open documentation (requires login)
- ⚠️ **CATIA** - CAA V5 docs (requires login)
- ✅ **Onshape** - REST API and FeatureScript
- ⚠️ **PTC Creo** - Toolkit docs (requires login)
- ✅ **FreeCAD** - Wiki and API reference
- ✅ **Blender** - Python API

### EDA/Electronics
- ✅ **KiCad** - Python API reference
- ⚠️ **Altium** - Scripting docs (requires login)
- ⚠️ **Cadence** - SKILL docs (requires login)

### BIM/Architecture
- ✅ **Revit** - .NET API documentation
- ✅ **AutoCAD** - ObjectARX/NET API
- ✅ **Rhino** - RhinoCommon API
- ✅ **Grasshopper** - SDK documentation

## 🔑 Authentication Setup

### Autodesk (Fusion 360, Inventor, Revit, AutoCAD)

1. Create app at: https://aps.autodesk.com/myapps
2. Get 3-legged OAuth token
3. Add to config:
```yaml
authentication:
  autodesk:
    type: oauth
    token: "YOUR_TOKEN"
```

### SolidWorks

1. Get MySolidWorks account
2. Add credentials:
```yaml
authentication:
  solidworks:
    type: form
    username: "email@example.com"
    password: "password"
```

### Onshape

1. Get API keys from: https://dev-portal.onshape.com/keys
2. Add to config:
```yaml
authentication:
  onshape:
    type: oauth
    access_key: "YOUR_ACCESS_KEY"
    secret_key: "YOUR_SECRET_KEY"
```

## 🔍 Search Interface

The search interface provides powerful full-text search:

```bash
# Interactive mode
python search_docs.py -i

# Search commands:
Search> fusion sketch api              # Basic search
Search> "exact phrase"                 # Phrase search
Search> site:fusion360 extrude        # Site-specific search
Search> title:api content:python      # Field search
Search> help                          # Show help
Search> stats                         # Index statistics
Search> sites                         # List indexed sites
```

## 📁 Output Structure

```
documentation_archive/
├── fusion360/
│   ├── api/
│   │   ├── sketch_api.md
│   │   └── feature_api.md
│   └── help/
│       └── tutorials.md
├── solidworks/
│   └── api/
│       └── sldworks_api.md
├── search_index/          # Whoosh search index
└── documentation_index.json  # Metadata index
```

## 🛠️ Advanced Usage

### Custom Site Parser

Create a custom parser for better extraction:

```python
# In site_parsers.py
class MyCustomParser(BaseParser):
    def extract_content(self, soup, url):
        # Custom extraction logic
        content = soup.select_one('.my-content')
        return content.get_text()

# Register parser
PARSERS['mysite'] = MyCustomParser()
```

### Parallel Scraping (Experimental)

For faster scraping of independent pages:

```bash
python doc_scraper.py --parallel --workers 4
```

### Export to Different Formats

```bash
# Export as single searchable HTML
python export_docs.py --format html --output docs.html

# Export as PDF (requires wkhtmltopdf)
python export_docs.py --format pdf --output docs.pdf
```

## ⚠️ Important Notes

1. **Respect Rate Limits**: Default is 1 second between requests. Adjust in config.
2. **Check Terms of Service**: Ensure you're allowed to scrape each site.
3. **Storage Requirements**: Full scrape can be 5-20GB depending on sites.
4. **Credentials Security**: Never commit config files with credentials!
5. **VPN/Proxy**: Some sites may require VPN access or have geographic restrictions.

## 🐛 Troubleshooting

### Selenium Issues

```bash
# Install Chrome and driver
brew install --cask google-chrome
brew install --cask chromedriver

# Or use webdriver-manager (auto-downloads driver)
pip install webdriver-manager
```

### Authentication Failures

1. Check credentials are correct
2. Some sites require 2FA - use app-specific passwords
3. Try Selenium mode for complex JS authentication:
```yaml
sites:
  mysite:
    use_selenium: true
```

### Rate Limiting

If you get blocked, increase rate limit:
```yaml
rate_limit: 2.0  # 2 seconds between requests
```

## 📊 Statistics

After scraping, check what you've collected:

```bash
python search_docs.py --stats

# Output:
# Total Documents: 15,234
# Index Size: 125.3 MB
# Sites: 12
# Last Updated: 2024-01-09 15:30:00
```

## 🔄 Updating Documentation

Run periodically to get latest docs:

```bash
# Incremental update (skips existing)
python doc_scraper.py --all --update

# Force re-download everything
python doc_scraper.py --all --force
```

## 🤝 Contributing

To add support for a new documentation site:

1. Add site configuration to `scraper_config.yaml`
2. Create custom parser in `site_parsers.py` if needed
3. Test with: `python doc_scraper.py --site newsite --test`

## 📄 License

This tool is for personal/educational use. Respect the terms of service and copyright of each documentation site.

## 🎯 Use with AI Agents

Once documentation is scraped and indexed, AI agents can quickly reference it:

```python
from doc_scraper.search_docs import DocumentationSearcher

searcher = DocumentationSearcher()
results = searcher.search("fusion 360 sketch constraint api")

for result in results:
    print(f"Found: {result['title']} in {result['site']}")
    print(f"Preview: {result['preview']}")
```

This provides AI agents with instant access to comprehensive API documentation for faster, more accurate code generation.

---

**Remember**: Always respect rate limits and terms of service. This tool is meant to create a personal reference library for development purposes.
