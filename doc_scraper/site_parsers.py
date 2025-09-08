"""
Site-specific parsers for better content extraction
Each parser is optimized for specific documentation formats
"""

import re
from typing import Dict, List, Optional, Tuple
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import json

class BaseParser:
    """Base parser class with common functionality"""
    
    def extract_content(self, soup: BeautifulSoup, url: str) -> str:
        """Extract main content from page"""
        raise NotImplementedError
    
    def extract_links(self, soup: BeautifulSoup, url: str) -> List[str]:
        """Extract documentation links from page"""
        links = []
        for link in soup.find_all('a', href=True):
            href = link['href']
            absolute_url = urljoin(url, href)
            
            # Filter documentation links
            if self.is_valid_link(absolute_url, url):
                links.append(absolute_url)
        
        return links
    
    def is_valid_link(self, link: str, base_url: str) -> bool:
        """Check if link should be followed"""
        # Skip external domains
        if urlparse(link).netloc != urlparse(base_url).netloc:
            return False
        
        # Skip non-documentation links
        skip_patterns = [
            r'/login', r'/logout', r'/download', r'/search',
            r'\.(pdf|zip|exe|dmg|pkg)$'
        ]
        
        for pattern in skip_patterns:
            if re.search(pattern, link, re.I):
                return False
        
        return True
    
    def extract_metadata(self, soup: BeautifulSoup) -> Dict:
        """Extract page metadata"""
        metadata = {}
        
        # Title
        title = soup.find('title')
        if title:
            metadata['title'] = title.get_text().strip()
        
        # Description
        desc = soup.find('meta', attrs={'name': 'description'})
        if desc:
            metadata['description'] = desc.get('content', '')
        
        # Keywords
        keywords = soup.find('meta', attrs={'name': 'keywords'})
        if keywords:
            metadata['keywords'] = keywords.get('content', '').split(',')
        
        return metadata


class AutodeskParser(BaseParser):
    """Parser for Autodesk documentation (Fusion 360, Inventor, Revit, AutoCAD)"""
    
    def extract_content(self, soup: BeautifulSoup, url: str) -> str:
        # Autodesk uses specific content containers
        content_selectors = [
            '.help-content',
            '.content-container',
            '#content',
            'article',
            '.topic-content'
        ]
        
        for selector in content_selectors:
            content = soup.select_one(selector)
            if content:
                # Remove navigation elements
                for nav in content.select('.nav, .breadcrumb, .toc'):
                    nav.decompose()
                
                return content.get_text(separator='\n', strip=True)
        
        # Fallback to body
        body = soup.find('body')
        return body.get_text(separator='\n', strip=True) if body else ''
    
    def extract_api_reference(self, soup: BeautifulSoup) -> Dict:
        """Extract API reference information"""
        api_info = {}
        
        # Look for API method signatures
        signatures = soup.select('.api-signature, .method-signature, code.signature')
        if signatures:
            api_info['signatures'] = [sig.get_text(strip=True) for sig in signatures]
        
        # Parameters
        param_tables = soup.select('table.parameters, .param-table')
        if param_tables:
            api_info['parameters'] = []
            for table in param_tables:
                params = []
                for row in table.select('tr')[1:]:  # Skip header
                    cells = row.select('td')
                    if len(cells) >= 2:
                        params.append({
                            'name': cells[0].get_text(strip=True),
                            'description': cells[1].get_text(strip=True)
                        })
                api_info['parameters'].extend(params)
        
        return api_info


class SolidWorksParser(BaseParser):
    """Parser for SolidWorks API documentation"""
    
    def extract_content(self, soup: BeautifulSoup, url: str) -> str:
        # SolidWorks specific selectors
        content_selectors = [
            '#main-content',
            '.topic',
            '#topic',
            '.content'
        ]
        
        for selector in content_selectors:
            content = soup.select_one(selector)
            if content:
                # Extract code examples
                code_blocks = content.select('pre, .code-block')
                code_examples = []
                for block in code_blocks:
                    code_examples.append(block.get_text(strip=True))
                
                # Get main text
                text = content.get_text(separator='\n', strip=True)
                
                # Append code examples
                if code_examples:
                    text += '\n\n## Code Examples:\n'
                    for i, code in enumerate(code_examples, 1):
                        text += f'\n### Example {i}:\n```\n{code}\n```\n'
                
                return text
        
        return soup.get_text(separator='\n', strip=True)


class OnshapeParser(BaseParser):
    """Parser for Onshape documentation and FeatureScript"""
    
    def extract_content(self, soup: BeautifulSoup, url: str) -> str:
        # Check if it's FeatureScript documentation
        if 'FsDoc' in url:
            return self.extract_featurescript(soup)
        
        # Regular documentation
        content_selectors = [
            '.doc-content',
            '.api-content',
            '#content',
            'main'
        ]
        
        for selector in content_selectors:
            content = soup.select_one(selector)
            if content:
                return content.get_text(separator='\n', strip=True)
        
        return soup.get_text(separator='\n', strip=True)
    
    def extract_featurescript(self, soup: BeautifulSoup) -> str:
        """Extract FeatureScript specific documentation"""
        content = []
        
        # Function signatures
        signatures = soup.select('.function-signature, .fs-signature')
        for sig in signatures:
            content.append(f"Function: {sig.get_text(strip=True)}")
        
        # Parameters and returns
        params = soup.select('.parameters, .param-list')
        for param in params:
            content.append(f"Parameters:\n{param.get_text(strip=True)}")
        
        # Examples
        examples = soup.select('.example, pre.code')
        for ex in examples:
            content.append(f"Example:\n```\n{ex.get_text(strip=True)}\n```")
        
        # Description
        desc = soup.select_one('.description, .doc-description')
        if desc:
            content.append(f"Description:\n{desc.get_text(strip=True)}")
        
        return '\n\n'.join(content)


class FreeCADParser(BaseParser):
    """Parser for FreeCAD wiki and API documentation"""
    
    def extract_content(self, soup: BeautifulSoup, url: str) -> str:
        # Remove wiki interface elements
        for element in soup.select('#mw-navigation, #footer, .printfooter, .catlinks'):
            element.decompose()
        
        # Get main content
        content = soup.select_one('#mw-content-text, #content, .mw-parser-output')
        
        if content:
            # Clean up wiki-specific elements
            for edit_link in content.select('.mw-editsection'):
                edit_link.decompose()
            
            # Extract code blocks properly
            code_blocks = content.select('pre, .mw-highlight')
            formatted_content = []
            
            # Get text sections
            for element in content.children:
                if element.name == 'pre' or 'mw-highlight' in str(element.get('class', [])):
                    formatted_content.append(f"```python\n{element.get_text(strip=True)}\n```")
                elif element.name:
                    formatted_content.append(element.get_text(separator='\n', strip=True))
            
            return '\n\n'.join(formatted_content)
        
        return soup.get_text(separator='\n', strip=True)


class BlenderParser(BaseParser):
    """Parser for Blender Python API documentation"""
    
    def extract_content(self, soup: BeautifulSoup, url: str) -> str:
        # Blender API specific selectors
        content_selectors = [
            '.document',
            '.body',
            '[role="main"]',
            '#main-content'
        ]
        
        for selector in content_selectors:
            content = soup.select_one(selector)
            if content:
                # Extract class/module information
                classes = content.select('.class, .py-class')
                class_info = []
                for cls in classes:
                    class_info.append(cls.get_text(strip=True))
                
                # Extract methods
                methods = content.select('.method, .py-method')
                method_info = []
                for method in methods:
                    method_info.append(method.get_text(strip=True))
                
                # Main content
                text = content.get_text(separator='\n', strip=True)
                
                # Add structured information
                if class_info:
                    text += '\n\n## Classes:\n' + '\n'.join(class_info)
                if method_info:
                    text += '\n\n## Methods:\n' + '\n'.join(method_info)
                
                return text
        
        return soup.get_text(separator='\n', strip=True)


class RhinoParser(BaseParser):
    """Parser for Rhino/Grasshopper documentation"""
    
    def extract_content(self, soup: BeautifulSoup, url: str) -> str:
        # Rhino developer docs structure
        content_selectors = [
            '.content',
            '#content',
            '.api-content',
            'article'
        ]
        
        for selector in content_selectors:
            content = soup.select_one(selector)
            if content:
                # Extract API signatures
                signatures = content.select('.signature, .api-signature')
                
                # Extract examples
                examples = content.select('.example, pre.code')
                
                # Build formatted content
                text = content.get_text(separator='\n', strip=True)
                
                if signatures:
                    text += '\n\n## API Signatures:\n'
                    for sig in signatures:
                        text += f"- {sig.get_text(strip=True)}\n"
                
                if examples:
                    text += '\n\n## Examples:\n'
                    for ex in examples:
                        text += f"```\n{ex.get_text(strip=True)}\n```\n"
                
                return text
        
        return soup.get_text(separator='\n', strip=True)


# Parser registry
PARSERS = {
    'fusion360': AutodeskParser(),
    'fusion360_api': AutodeskParser(),
    'inventor': AutodeskParser(),
    'revit': AutodeskParser(),
    'autocad': AutodeskParser(),
    'solidworks': SolidWorksParser(),
    'onshape': OnshapeParser(),
    'onshape_rest': OnshapeParser(),
    'freecad': FreeCADParser(),
    'freecad_source': FreeCADParser(),
    'blender': BlenderParser(),
    'rhino': RhinoParser(),
    'grasshopper': RhinoParser(),
}

def get_parser(site_name: str) -> BaseParser:
    """Get appropriate parser for a site"""
    return PARSERS.get(site_name, BaseParser())
