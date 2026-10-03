#!/usr/bin/env python3
import os
import re
import sys
import urllib.request
import urllib.parse
import time
from html.parser import HTMLParser

# Default target directory
DEFAULT_OUTPUT_DIR = "./livros/"

# HTML parser to extract books from search table
class LibgenTableParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.in_table = False
        self.in_tbody = False
        self.in_row = False
        self.in_cell = False
        self.in_link = False
        self.col_index = -1
        self.current_row = []
        self.current_cell_text = []
        self.current_cell_links = []
        self.current_link = None
        self.rows = []

    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        
        if tag == 'table' and attrs_dict.get('id') == 'tablelibgen':
            self.in_table = True
            
        if not self.in_table:
            return
            
        if tag == 'tbody':
            self.in_tbody = True
            
        if tag == 'tr' and self.in_tbody:
            self.in_row = True
            self.col_index = -1
            self.current_row = []
            
        if tag == 'td' and self.in_row:
            self.in_cell = True
            self.col_index += 1
            self.current_cell_text = []
            self.current_cell_links = []
            
        if tag == 'a' and self.in_cell:
            self.in_link = True
            href = attrs_dict.get('href', '')
            title = attrs_dict.get('title', '')
            self.current_link = {'href': href, 'title': title, 'text': []}

    def handle_data(self, data):
        if self.in_link:
            self.current_link['text'].append(data)
        if self.in_cell:
            self.current_cell_text.append(data)

    def handle_endtag(self, tag):
        if not self.in_table:
            return
            
        if tag == 'table':
            self.in_table = False
            self.in_tbody = False
            
        if tag == 'tbody':
            self.in_tbody = False
            
        if tag == 'tr' and self.in_row:
            self.in_row = False
            if self.current_row:
                self.rows.append(self.current_row)
                
        if tag == 'td' and self.in_cell:
            self.in_cell = False
            cell_data = {
                'text': ''.join(self.current_cell_text).strip(),
                'links': self.current_cell_links
            }
            self.current_row.append(cell_data)
            
        if tag == 'a' and self.in_link:
            self.in_link = False
            link_text = ''.join(self.current_link['text']).strip()
            self.current_link['text'] = link_text
            self.current_cell_links.append(self.current_link)
            self.current_link = None

# HTML parser to extract download URL from individual book page
class LibgenDownloadParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.download_url = None

    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        if tag == 'a':
            href = attrs_dict.get('href', '')
            if 'get.php?md5=' in href or 'get.php?key=' in href:
                self.download_url = href

# Format size in human readable form
def format_size(size_bytes):
    size = float(size_bytes)
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size < 1024:
            return f"{size:.2f} {unit}"
        size /= 1024
    return f"{size:.2f} TB"

# Sanitize name to generate safe filename
def sanitize_filename(name):
    cleaned = re.sub(r'[\\/*?:"<>|]', "", name)
    cleaned = cleaned.replace(" ", "_")
    return cleaned[:150]

# Display beautiful colorful results table
def render_books_table(books):
    if not books:
        print("\033[91mNo books matched the search criteria.\033[0m")
        return
        
    print("\n\033[95m" + "="*125 + "\033[0m")
    print(f"\033[96m{'IDX':<4} | {'TITLE':<55} | {'AUTHOR(S)':<25} | {'YEAR':<5} | {'SIZE':<8} | {'EXT':<4}\033[0m")
    print("\033[95m" + "-"*125 + "\033[0m")
    for b in books:
        title = b['title']
        if len(title) > 53:
            title = title[:50] + "..."
        authors = b['authors']
        if len(authors) > 23:
            authors = authors[:20] + "..."
            
        print(f"\033[92m{b['index']:<4}\033[0m | {title:<55} | {authors:<25} | {b['year']:<5} | {b['size']:<8} | \033[93m{b['extension']:<4}\033[0m")
    print("\033[95m" + "="*125 + "\033[0m\n")

# Connect to URL using urllib
def fetch_url(url, referer=None):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }
    if referer:
        headers['Referer'] = referer
        
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=20) as resp:
        return resp.read(), resp.info()

# Download helper with premium progress bar
def download_file(url, output_path, fallback_filename, referer=None):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }
    if referer:
        headers['Referer'] = referer
        
    req = urllib.request.Request(url, headers=headers)
    
    print(f"\033[94mConnecting to download gateway...\033[0m")
    with urllib.request.urlopen(req, timeout=30) as resp:
        # Determine actual filename
        cd = resp.info().get('Content-Disposition', '')
        filename = fallback_filename
        
        match = re.search(r'filename="([^"]+)"', cd)
        if match:
            filename = match.group(1)
        else:
            match = re.search(r'filename=([^;]+)', cd)
            if match:
                filename = match.group(1).strip()
                
        # Sanitize filename and truncate to avoid OS name-too-long limits
        filename = re.sub(r'[\\/*?:"<>|]', "", filename)
        name_parts = os.path.splitext(filename)
        base = name_parts[0][:130].strip()
        ext = name_parts[1].lower().strip()
        filename = base + ext
        final_dest = os.path.join(output_path, filename)
        
        # Content Length
        total_size = resp.info().get('Content-Length')
        total_size = int(total_size) if total_size else None
        
        print(f"\033[32mFile Name: {filename}\033[0m")
        if total_size:
            print(f"\033[32mFile Size: {format_size(total_size)}\033[0m")
        else:
            print(f"\033[33mFile Size: Unknown (Streaming mode)\033[0m")
            
        # Stream data
        start_time = time.time()
        downloaded = 0
        block_size = 8192
        
        with open(final_dest, 'wb') as f:
            while True:
                buffer = resp.read(block_size)
                if not buffer:
                    break
                f.write(buffer)
                downloaded += len(buffer)
                
                # Render premium progress bar
                elapsed = time.time() - start_time
                if elapsed == 0:
                    elapsed = 0.001
                speed = downloaded / elapsed
                speed_str = format_size(speed) + "/s"
                downloaded_str = format_size(downloaded)
                
                if total_size:
                    percent = (downloaded / total_size) * 100
                    total_str = format_size(total_size)
                    bar_length = 30
                    filled_length = int(bar_length * downloaded // total_size)
                    bar = '█' * filled_length + '░' * (bar_length - filled_length)
                    
                    # ETA calculation
                    remaining_bytes = total_size - downloaded
                    remaining_time = remaining_bytes / speed if speed > 0 else 0
                    if remaining_time > 60:
                        eta_str = f"{int(remaining_time//60)}m {int(remaining_time%60)}s"
                    else:
                        eta_str = f"{remaining_time:.1f}s"
                        
                    sys.stdout.write(f"\r\033[94m[{bar}] {percent:.1f}% ({downloaded_str}/{total_str}) | {speed_str} | ETA: {eta_str}\033[0m")
                else:
                    sys.stdout.write(f"\r\033[94mDownloaded: {downloaded_str} | {speed_str} | Elapsed: {elapsed:.1f}s\033[0m")
                sys.stdout.flush()
                
        print(f"\n\033[92m✔ Download completed successfully!\033[0m")
        print(f"\033[96mSaved file to: {final_dest}\033[0m\n")
        return final_dest

# Perform search and parse results
def search_libgen(query, ext_pref='epub', max_results=10):
    # topics[]=l restricts search to libgen (books) only, excluding scimag (journal articles)
    url = f"https://libgen.li/index.php?req={urllib.parse.quote(query)}&topics[]=l"
    print(f"\033[94mSearching LibGen mirror for: '{query}'...\033[0m")
    
    try:
        html, _ = fetch_url(url)
    except Exception as e:
        print(f"\033[91mConnection error querying LibGen mirror: {e}\033[0m")
        return []
        
    parser = LibgenTableParser()
    parser.feed(html.decode('utf-8', errors='ignore'))
    
    books = []
    for row in parser.rows:
        if len(row) < 9:
            continue
            
        col0 = row[0]
        edition_links = [l for l in col0['links'] if 'edition.php' in l['href']]
        
        # Clean title heuristic
        title = ""
        if len(edition_links) >= 2:
            title = edition_links[1]['text']
        elif len(edition_links) == 1:
            title = edition_links[0]['text']
            
        if not title:
            non_empty_links = [l for l in col0['links'] if l['text'] and not l['text'].startswith('DOI:') and not any(char.isdigit() for char in l['text'][:5])]
            if non_empty_links:
                title = non_empty_links[0]['text']
            else:
                title = col0['text']
                
        series_links = [l for l in col0['links'] if 'series.php' in l['href']]
        series = series_links[0]['text'] if series_links else ""

        authors = row[1]['text']
        publisher = row[2]['text']
        year = row[3]['text']
        language = row[4]['text']
        pages = row[5]['text']
        size = row[6]['text']
        extension = row[7]['text'].lower().strip()
        
        mirrors = row[8]['links']
        ads_href = ""
        for m in mirrors:
            if 'ads.php' in m['href']:
                ads_href = m['href']
                break
                
        books.append({
            'title': title,
            'series': series,
            'authors': authors,
            'publisher': publisher,
            'year': year,
            'language': language,
            'pages': pages,
            'size': size,
            'extension': extension,
            'ads_href': ads_href
        })
        
    # Filter by extension preference
    ext_pref = ext_pref.lower().strip()
    if ext_pref != 'all':
        primary = [b for b in books if b['extension'] == ext_pref]
        secondary = [b for b in books if b['extension'] != ext_pref]
        # Keep preferred extension at the top
        sorted_books = primary + secondary
    else:
        sorted_books = books
        
    # Cap results and assign incremental index
    final_books = []
    for idx, b in enumerate(sorted_books[:max_results]):
        b['index'] = idx + 1
        final_books.append(b)
        
    return final_books

# Orchestrate individual download
def download_book_selection(book, output_dir):
    if not book['ads_href']:
        print("\033[91mError: No download mirror link available for this book.\033[0m")
        return None

    # Construct expected path to check for duplicates before hitting mirrors
    clean_title = sanitize_filename(book['title'])
    match_title = clean_title[:20].lower().replace("_", "")
    
    if os.path.exists(output_dir):
        for existing_file in os.listdir(output_dir):
            existing_clean = sanitize_filename(existing_file).lower().replace("_", "")
            if match_title in existing_clean and existing_file.lower().endswith(book['extension'].lower()):
                found_path = os.path.join(output_dir, existing_file)
                print(f"\n\033[92m✔ Book already downloaded (matched by title): {found_path}\033[0m\n")
                return found_path
        
    ads_url = f"https://libgen.li{book['ads_href']}"
    print(f"\033[94mFetching mirror landing page...\033[0m")
    
    try:
        ads_html, _ = fetch_url(ads_url)
    except Exception as e:
        print(f"\033[91mFailed to connect to mirror gateway: {e}\033[0m")
        return None
        
    # Extract the actual download gateway URL
    dl_parser = LibgenDownloadParser()
    dl_parser.feed(ads_html.decode('utf-8', errors='ignore'))
    
    if not dl_parser.download_url:
        print("\033[91mError: Could not locate direct download ('GET') link in mirror HTML.\033[0m")
        return None
        
    direct_dl_url = f"https://libgen.li/{dl_parser.download_url}"
    
    # Construct fallback filename
    clean_title = sanitize_filename(book['title'])
    clean_author = sanitize_filename(book['authors'].split(';')[0])
    fallback_name = f"{clean_title}_-_({clean_author}).{book['extension']}"
    
    # Run the download stream
    try:
        os.makedirs(output_dir, exist_ok=True)
        return download_file(direct_dl_url, output_dir, fallback_name, referer=ads_url)
    except Exception as e:
        print(f"\033[91mDownload failed due to network or write error: {e}\033[0m")
        return None

def parse_args():
    import argparse
    parser = argparse.ArgumentParser(description="Raspador e Download de Livros Modernos (LibGen)")
    parser.add_argument("-q", "--query", type=str, help="Search terms / book title")
    parser.add_argument("-e", "--ext", type=str, default="epub", choices=["epub", "pdf", "all"], help="Preferred extension (default: epub)")
    parser.add_argument("-o", "--output-dir", type=str, default=DEFAULT_OUTPUT_DIR, help=f"Destination directory (default: {DEFAULT_OUTPUT_DIR})")
    parser.add_argument("-n", "--max-results", type=int, default=10, help="Maximum number of search results to list (default: 10)")
    parser.add_argument("-i", "--index", type=int, help="Directly download matching book index (1-based), skips interactive menu")
    parser.add_argument("-y", "--yes", action="store_true", help="Auto-download the first match without prompting")
    return parser.parse_args()

def main():
    args = parse_args()
    
    # If no query is provided via args, prompt the user interactively
    query = args.query
    if not query:
        print("\n\033[95m📚 RASPADOR DE LIVROS MODERNOS (LIBGEN) 📚\033[0m")
        try:
            query = input("\033[96mEnter your book title/search query: \033[0m").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nExiting.")
            sys.exit(0)
            
    if not query:
        print("\033[91mError: Search query cannot be empty.\033[0m")
        sys.exit(1)
        
    books = search_libgen(query, ext_pref=args.ext, max_results=args.max_results)
    if not books:
        print("\033[91mNo books found.\033[0m")
        sys.exit(0)
        
    # Render table
    render_books_table(books)
    
    selected_book = None
    
    # Non-interactive CLI direct selections
    if args.index is not None:
        idx = args.index
        if 1 <= idx <= len(books):
            selected_book = books[idx - 1]
        else:
            print(f"\033[91mError: Provided index {idx} is out of bounds (1-{len(books)}).\033[0m")
            sys.exit(1)
    elif args.yes:
        # Download first match automatically
        selected_book = books[0]
        print(f"\033[33mOption --yes provided. Auto-selecting first match: '{selected_book['title']}'...\033[0m")
    else:
        # Interactive shell prompt
        while True:
            try:
                choice = input(f"\033[96mSelect a book index to download (1-{len(books)}) or 'q' to quit: \033[0m").strip().lower()
            except (KeyboardInterrupt, EOFError):
                print("\nExiting.")
                sys.exit(0)
                
            if choice in ['q', 'quit', 'exit']:
                print("Exiting.")
                sys.exit(0)
            try:
                idx = int(choice)
                if 1 <= idx <= len(books):
                    selected_book = books[idx - 1]
                    break
                else:
                    print(f"\033[91mPlease select a number between 1 and {len(books)}.\033[0m")
            except ValueError:
                print("\033[91mInvalid input. Please enter a valid number or 'q'.\033[0m")
                
    if selected_book:
        print(f"\n\033[95mSelected book:\033[0m '{selected_book['title']}' [\033[93m{selected_book['extension']}\033[0m]")
        download_book_selection(selected_book, args.output_dir)

if __name__ == "__main__":
    main()
