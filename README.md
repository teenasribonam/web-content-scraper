# Web Content Scraper

A Python-based web content extraction system that accepts a user search query, retrieves search result URLs, opens the webpages using Playwright, extracts visible web content, and stores the collected data in JSON format.

## Features

- Accepts user-defined search queries
- Retrieves top search result URLs
- Automates browser interaction using Playwright
- Handles dynamically loaded webpage content
- Automatically scrolls webpages before extraction
- Extracts headings, paragraphs, links, images, buttons, lists, and code blocks
- Removes duplicate extracted content
- Handles page timeouts and extraction errors
- Stores scraped results in JSON format

## Tech Stack

- Python
- Playwright
- DDGS
- JSON

## How It Works

```text
User Search Query
       ↓
Web Search
       ↓
Top Search Result URLs
       ↓
Playwright Browser
       ↓
Open Each Webpage
       ↓
Auto Scroll
       ↓
Extract Visible Content
       ↓
Remove Duplicates
       ↓
JSON Output
```

## Project Structure

```text
web-content-scraper/
│
├── browser.py          # Browser and Playwright management
├── config.py           # Scraper configuration
├── search.py           # Search result URL extraction
├── extractor.py        # Webpage content extraction
├── writer.py            # JSON output handling
├── main.py              # Main application workflow
├── scraped_data.json    # Scraped output
└── README.md            # Project documentation
```

## Installation

Clone the repository:

```bash
git clone https://github.com/teenasribonam/web-content-scraper.git
```

Move into the project directory:

```bash
cd web-content-scraper
```

Install the required Python packages:

```bash
pip install playwright ddgs
```

Install the Playwright browser:

```bash
playwright install chromium
```

## Usage

Run the application:

```bash
python main.py
```

Enter a search query when prompted:

```text
Enter Search Query: Python programming
```

The application searches for relevant URLs, opens the webpages, extracts their visible content, and stores the collected results in:

```text
scraped_data.json
```

## Output

The JSON output contains information such as:

- Page URL
- Page title
- Headings
- Paragraph text
- Links and their URLs
- Image sources and alt text
- Buttons
- Code blocks
- Lists

Example structure:

```json
[
    {
        "url": "https://example.com",
        "title": "Example Website",
        "blocks": [
            {
                "type": "h1",
                "text": "Example Heading"
            },
            {
                "type": "p",
                "text": "Example paragraph"
            },
            {
                "type": "link",
                "text": "Example Link",
                "url": "https://example.com/page"
            }
        ]
    }
]
```

## Error Handling

The scraper handles webpage timeouts and other extraction errors without stopping the entire scraping process. Failed pages are recorded with an error status while the remaining URLs continue to be processed.

## Author

Teena Sri Bonam
