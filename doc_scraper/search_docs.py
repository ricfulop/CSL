#!/usr/bin/env python3
"""
Interactive search interface for scraped documentation
Provides fast full-text search with ranking and preview
"""

import os
import json
import re
from pathlib import Path
from typing import List, Dict, Optional, Tuple
import argparse
from datetime import datetime

from whoosh import index
from whoosh.fields import Schema, TEXT, ID, NUMERIC, DATETIME, KEYWORD
from whoosh.qparser import QueryParser, MultifieldParser
from whoosh.query import And, Or, Term, Phrase
from whoosh import scoring
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.syntax import Syntax
from rich.prompt import Prompt
from rich import print as rprint
import pickle

console = Console()

class DocumentationSearcher:
    """Full-text search for scraped documentation"""
    
    def __init__(self, base_dir: str = "documentation_archive"):
        self.base_dir = Path(base_dir)
        self.index_dir = self.base_dir / "search_index"
        self.index_dir.mkdir(parents=True, exist_ok=True)
        
        # Define search schema
        self.schema = Schema(
            path=ID(stored=True, unique=True),
            title=TEXT(stored=True, field_boost=2.0),
            content=TEXT(stored=True),
            site=KEYWORD(stored=True, commas=True),
            url=ID(stored=True),
            file_path=ID(stored=True),
            word_count=NUMERIC(stored=True),
            indexed_at=DATETIME(stored=True)
        )
        
        self._ix = None
        
    @property
    def ix(self):
        """Lazy load or create index"""
        if self._ix is None:
            if index.exists_in(str(self.index_dir)):
                self._ix = index.open_dir(str(self.index_dir))
            else:
                self._ix = index.create_in(str(self.index_dir), self.schema)
        return self._ix
    
    def build_index(self, force_rebuild: bool = False):
        """Build search index from scraped documentation"""
        if not force_rebuild and index.exists_in(str(self.index_dir)):
            console.print("[yellow]Index already exists. Use --rebuild to force rebuild.[/yellow]")
            return
        
        console.print("[cyan]Building search index...[/cyan]")
        
        # Create new index
        ix = index.create_in(str(self.index_dir), self.schema)
        writer = ix.writer()
        
        # Walk through all markdown files
        doc_count = 0
        for md_file in self.base_dir.rglob("*.md"):
            if 'search_index' in str(md_file):
                continue
            
            try:
                # Read file
                with open(md_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Extract metadata from frontmatter
                metadata = {}
                if content.startswith('---'):
                    parts = content.split('---', 2)
                    if len(parts) >= 3:
                        meta_text = parts[1]
                        content = parts[2]
                        
                        for line in meta_text.strip().split('\n'):
                            if ':' in line:
                                key, value = line.split(':', 1)
                                metadata[key.strip()] = value.strip()
                
                # Extract title
                title = metadata.get('title', '')
                if not title:
                    # Try to extract from first H1
                    title_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
                    if title_match:
                        title = title_match.group(1)
                    else:
                        title = md_file.stem.replace('_', ' ').title()
                
                # Determine site from path
                relative_path = md_file.relative_to(self.base_dir)
                site = relative_path.parts[0] if relative_path.parts else 'unknown'
                
                # Add to index
                writer.add_document(
                    path=str(md_file),
                    title=title,
                    content=content,
                    site=site,
                    url=metadata.get('url', ''),
                    file_path=str(relative_path),
                    word_count=len(content.split()),
                    indexed_at=datetime.now()
                )
                
                doc_count += 1
                
                if doc_count % 100 == 0:
                    console.print(f"  Indexed {doc_count} documents...")
                    
            except Exception as e:
                console.print(f"[red]Error indexing {md_file}: {e}[/red]")
                continue
        
        writer.commit()
        console.print(f"[green]✓ Indexed {doc_count} documents[/green]")
        
        # Reset cached index
        self._ix = None
    
    def search(self, query_str: str, site: Optional[str] = None, 
               limit: int = 10, show_preview: bool = True) -> List[Dict]:
        """Search documentation with optional site filtering"""
        
        with self.ix.searcher(weighting=scoring.BM25F()) as searcher:
            # Parse query for multiple fields
            parser = MultifieldParser(["title", "content"], schema=self.ix.schema)
            query = parser.parse(query_str)
            
            # Add site filter if specified
            if site:
                site_filter = Term("site", site)
                query = And([query, site_filter])
            
            # Execute search
            results = searcher.search(query, limit=limit)
            
            # Format results
            formatted_results = []
            for hit in results:
                result = {
                    'title': hit['title'],
                    'site': hit['site'],
                    'url': hit.get('url', ''),
                    'file_path': hit['file_path'],
                    'score': hit.score,
                    'word_count': hit.get('word_count', 0)
                }
                
                if show_preview:
                    # Get content preview with highlights
                    content = hit['content']
                    # Find best matching snippet
                    snippet = self._extract_snippet(content, query_str)
                    result['preview'] = snippet
                
                formatted_results.append(result)
            
            return formatted_results
    
    def _extract_snippet(self, content: str, query: str, context_size: int = 150) -> str:
        """Extract relevant snippet from content"""
        # Simple keyword-based snippet extraction
        query_terms = query.lower().split()
        lines = content.split('\n')
        
        best_snippet = ""
        best_score = 0
        
        for i, line in enumerate(lines):
            line_lower = line.lower()
            
            # Count query term occurrences
            score = sum(1 for term in query_terms if term in line_lower)
            
            if score > best_score:
                best_score = score
                
                # Get context
                start = max(0, i - 1)
                end = min(len(lines), i + 2)
                snippet_lines = lines[start:end]
                
                # Join and truncate
                snippet = ' '.join(snippet_lines)
                if len(snippet) > context_size * 2:
                    snippet = snippet[:context_size] + "..." + snippet[-context_size:]
                
                best_snippet = snippet
        
        # Highlight query terms
        for term in query_terms:
            best_snippet = re.sub(
                f'({re.escape(term)})',
                r'**\1**',
                best_snippet,
                flags=re.IGNORECASE
            )
        
        return best_snippet if best_snippet else content[:context_size] + "..."
    
    def get_stats(self) -> Dict:
        """Get index statistics"""
        with self.ix.searcher() as searcher:
            return {
                'total_documents': searcher.doc_count(),
                'index_size': sum(f.stat().st_size for f in self.index_dir.glob('*')),
                'sites': list(searcher.lexicon("site")),
                'last_updated': datetime.fromtimestamp(
                    max(f.stat().st_mtime for f in self.index_dir.glob('*'))
                )
            }
    
    def interactive_search(self):
        """Interactive search interface"""
        console.print(Panel.fit(
            "[bold cyan]Documentation Search Interface[/bold cyan]\n"
            "Search through all scraped API documentation\n"
            "Commands: 'help', 'stats', 'sites', 'quit'"
        ))
        
        while True:
            # Get query
            query = Prompt.ask("\n[bold green]Search[/bold green]")
            
            if query.lower() == 'quit':
                break
            elif query.lower() == 'help':
                self._show_help()
                continue
            elif query.lower() == 'stats':
                self._show_stats()
                continue
            elif query.lower() == 'sites':
                self._show_sites()
                continue
            
            # Check for site filter
            site_filter = None
            if 'site:' in query:
                parts = query.split('site:', 1)
                if len(parts) == 2:
                    site_parts = parts[1].split(None, 1)
                    site_filter = site_parts[0]
                    query = parts[0] + (site_parts[1] if len(site_parts) > 1 else '')
            
            # Perform search
            try:
                results = self.search(query.strip(), site=site_filter, limit=10)
                
                if results:
                    self._display_results(results)
                    
                    # Ask if user wants to open a result
                    choice = Prompt.ask(
                        "\n[yellow]Enter result number to view (or press Enter to continue)[/yellow]",
                        default=""
                    )
                    
                    if choice.isdigit():
                        idx = int(choice) - 1
                        if 0 <= idx < len(results):
                            self._view_document(results[idx])
                else:
                    console.print("[yellow]No results found[/yellow]")
                    
            except Exception as e:
                console.print(f"[red]Search error: {e}[/red]")
    
    def _display_results(self, results: List[Dict]):
        """Display search results in a table"""
        table = Table(title="Search Results", show_lines=True)
        table.add_column("#", style="cyan", width=3)
        table.add_column("Title", style="green", width=40)
        table.add_column("Site", style="yellow", width=15)
        table.add_column("Score", style="magenta", width=8)
        table.add_column("Preview", style="white", width=60)
        
        for i, result in enumerate(results, 1):
            preview = result.get('preview', '')[:100] + "..."
            table.add_row(
                str(i),
                result['title'][:40],
                result['site'],
                f"{result['score']:.2f}",
                preview
            )
        
        console.print(table)
    
    def _view_document(self, result: Dict):
        """View full document"""
        file_path = self.base_dir / result['file_path']
        
        if file_path.exists():
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Skip frontmatter
            if content.startswith('---'):
                parts = content.split('---', 2)
                if len(parts) >= 3:
                    content = parts[2]
            
            console.print(Panel(
                content[:3000] + ("\n\n[dim]... (truncated)[/dim]" if len(content) > 3000 else ""),
                title=f"[bold]{result['title']}[/bold]",
                subtitle=f"[dim]{result['file_path']}[/dim]"
            ))
        else:
            console.print(f"[red]File not found: {file_path}[/red]")
    
    def _show_help(self):
        """Show help information"""
        help_text = """
[bold cyan]Search Syntax:[/bold cyan]
• Simple search: [green]fusion api[/green]
• Phrase search: [green]"exact phrase"[/green]
• Site filter: [green]site:fusion360 sketch api[/green]
• Field search: [green]title:api content:python[/green]

[bold cyan]Commands:[/bold cyan]
• [yellow]help[/yellow] - Show this help
• [yellow]stats[/yellow] - Show index statistics
• [yellow]sites[/yellow] - List available sites
• [yellow]quit[/yellow] - Exit
        """
        console.print(Panel(help_text, title="Help"))
    
    def _show_stats(self):
        """Show index statistics"""
        stats = self.get_stats()
        
        table = Table(title="Index Statistics")
        table.add_column("Metric", style="cyan")
        table.add_column("Value", style="green")
        
        table.add_row("Total Documents", str(stats['total_documents']))
        table.add_row("Index Size", f"{stats['index_size'] / 1024 / 1024:.2f} MB")
        table.add_row("Sites", str(len(stats['sites'])))
        table.add_row("Last Updated", stats['last_updated'].strftime("%Y-%m-%d %H:%M:%S"))
        
        console.print(table)
    
    def _show_sites(self):
        """Show available sites"""
        stats = self.get_stats()
        
        table = Table(title="Available Sites")
        table.add_column("Site", style="cyan")
        
        for site in sorted(stats['sites']):
            if isinstance(site, bytes):
                site = site.decode('utf-8')
            table.add_row(site)
        
        console.print(table)


def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(description='Search scraped documentation')
    parser.add_argument('query', nargs='*', help='Search query')
    parser.add_argument('--build', action='store_true', help='Build search index')
    parser.add_argument('--rebuild', action='store_true', help='Force rebuild index')
    parser.add_argument('--site', help='Filter by site')
    parser.add_argument('--limit', type=int, default=10, help='Number of results')
    parser.add_argument('--interactive', '-i', action='store_true', help='Interactive mode')
    parser.add_argument('--dir', default='documentation_archive', help='Documentation directory')
    
    args = parser.parse_args()
    
    searcher = DocumentationSearcher(args.dir)
    
    if args.build or args.rebuild:
        searcher.build_index(force_rebuild=args.rebuild)
    
    elif args.interactive or not args.query:
        searcher.interactive_search()
    
    else:
        # Command-line search
        query = ' '.join(args.query)
        results = searcher.search(query, site=args.site, limit=args.limit)
        
        if results:
            for i, result in enumerate(results, 1):
                rprint(f"\n[bold cyan]{i}. {result['title']}[/bold cyan]")
                rprint(f"   [yellow]Site:[/yellow] {result['site']}")
                rprint(f"   [yellow]Score:[/yellow] {result['score']:.2f}")
                if result.get('url'):
                    rprint(f"   [yellow]URL:[/yellow] {result['url']}")
                rprint(f"   [yellow]File:[/yellow] {result['file_path']}")
                if result.get('preview'):
                    rprint(f"   [dim]{result['preview']}[/dim]")
        else:
            rprint("[yellow]No results found[/yellow]")


if __name__ == '__main__':
    main()
