#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Automated Intranet Daily Digest Generator
Performs web searches and uses Claude API to generate digest
"""

import json
import sys
import os
import requests
from datetime import datetime
from pathlib import Path
import anthropic

# Fix Windows console encoding
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    sys.stderr.reconfigure(encoding='utf-8', errors='replace')

# Get the directory where this script is located
SCRIPT_DIR = Path(__file__).parent

def log(message):
    """Print with timestamp"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] {message}")

def load_config():
    """Load API configuration"""
    config_path = SCRIPT_DIR / "api_config.json"

    if not config_path.exists():
        raise FileNotFoundError(
            f"API configuration file not found: {config_path}\n"
            "Please create api_config.json from api_config.json.template"
        )

    with open(config_path, 'r') as f:
        config = json.load(f)

    # Validate required fields
    required_fields = ['claude_api_key', 'search_api_key', 'search_provider']
    missing_fields = [field for field in required_fields if field not in config]

    if missing_fields:
        raise ValueError(f"Missing required fields in api_config.json: {', '.join(missing_fields)}")

    return config

def search_serpapi(query, api_key):
    """Perform search using SerpAPI"""
    url = "https://serpapi.com/search"
    params = {
        'q': query,
        'api_key': api_key,
        'num': 10,  # Get 10 results per search
        'engine': 'google'
    }

    try:
        response = requests.get(url, params=params, timeout=30)
        response.raise_for_status()
        data = response.json()

        # Extract organic results
        results = []
        for item in data.get('organic_results', [])[:10]:
            results.append({
                'title': item.get('title', ''),
                'link': item.get('link', ''),
                'snippet': item.get('snippet', '')
            })

        return results

    except requests.RequestException as e:
        log(f"Search error for query '{query}': {e}")
        return []

def search_google_custom(query, api_key, cx):
    """Perform search using Google Custom Search API"""
    url = "https://www.googleapis.com/customsearch/v1"
    params = {
        'key': api_key,
        'cx': cx,
        'q': query,
        'num': 10
    }

    try:
        response = requests.get(url, params=params, timeout=30)
        response.raise_for_status()
        data = response.json()

        results = []
        for item in data.get('items', []):
            results.append({
                'title': item.get('title', ''),
                'link': item.get('link', ''),
                'snippet': item.get('snippet', '')
            })

        return results

    except requests.RequestException as e:
        log(f"Search error for query '{query}': {e}")
        return []

def perform_searches(config):
    """Perform all web searches"""
    log("Starting web searches...")

    queries = [
        "SharePoint Viva intranet new feature launch announcement 2026",
        "employee experience platform product release announcement 2026",
        "Wix Squarespace Webflow Framer new feature release 2026",
        "v0.dev bolt.new lovable Replit Agent new release announcement 2026",
        "AI prototype to code tool launch announcement 2026",
        "figma AI code generation new feature release 2026",
        "enterprise intranet employee experience AI tools industry trends report 2026"
    ]

    all_results = {}

    for i, query in enumerate(queries, 1):
        log(f"Search {i}/{len(queries)}: {query[:50]}...")

        if config['search_provider'] == 'serpapi':
            results = search_serpapi(query, config['search_api_key'])
        elif config['search_provider'] == 'google_custom':
            results = search_google_custom(
                query,
                config['search_api_key'],
                config.get('google_cx', '')
            )
        else:
            raise ValueError(f"Unknown search provider: {config['search_provider']}")

        all_results[query] = results
        log(f"  Found {len(results)} results")

    return all_results

def generate_digest_with_claude(search_results, config):
    """Use Claude API to generate digest from search results"""
    log("Generating digest with Claude API...")

    # Format search results for Claude
    search_summary = ""
    for query, results in search_results.items():
        search_summary += f"\n\n## Search Query: {query}\n\n"
        for result in results:
            search_summary += f"**{result['title']}**\n"
            search_summary += f"Link: {result['link']}\n"
            search_summary += f"Snippet: {result['snippet']}\n\n"

    prompt = f"""You are generating a weekly email digest covering enterprise intranets, employee experience platforms, consumer website builders, and AI-native tools.

Based on the search results below, create a digest with 15-20 items organized into these categories:
- 🏢 Enterprise Intranets (4-5 items)
- 👥 Employee Experience Platforms (4-5 items)
- 🌐 Consumer Website Builders (3-4 items)
- 🤖 AI-Native Builders & Prototype-to-Code (5-6 items)

For each item:
1. Extract the most newsworthy, recent, and actionable information
2. Create a compelling title
3. Write a 1-2 sentence summary
4. Include the source link

Return ONLY valid HTML content (the body of the email, not a full HTML document). Use this exact structure:

<h1>Intranet Weekly Digest - {datetime.now().strftime('%B %d, %Y')}</h1>

<p class="greeting">Good morning,</p>
<p class="greeting">Here are this week's top updates on enterprise intranets, employee experience platforms, website builders, and AI-native tools.</p>

<h2>🏢 Enterprise Intranets <span class="category-count">(X items)</span></h2>

<div class="item">
    <div class="item-title">Title Here</div>
    <div class="item-description">Description here.</div>
    <div class="item-source">Source: <a href="URL">Link Text</a></div>
</div>

[Repeat for all items in all categories]

<div class="footer">
    <p>Generated by Kripal's Intranet Weekly Digest Agent | Created in Claude Code</p>
    <p>{datetime.now().strftime('%B %d, %Y')}</p>
</div>

SEARCH RESULTS:
{search_summary}
"""

    try:
        client = anthropic.Anthropic(api_key=config['claude_api_key'])

        message = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=8000,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        digest_body = message.content[0].text
        log(f"✓ Digest generated ({len(digest_body)} characters)")
        return digest_body

    except Exception as e:
        log(f"Error generating digest with Claude: {e}")
        raise

def wrap_html(body_content):
    """Wrap body content in full HTML structure"""
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Intranet Weekly Digest - {datetime.now().strftime('%B %d, %Y')}</title>
    <style>
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
            line-height: 1.6;
            color: #333;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            background-color: #f5f5f5;
        }}
        .container {{
            background-color: white;
            border-radius: 8px;
            padding: 30px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        }}
        h1 {{
            color: #667eea;
            border-bottom: 3px solid #667eea;
            padding-bottom: 10px;
            margin-bottom: 20px;
        }}
        h2 {{
            color: #555;
            margin-top: 30px;
            margin-bottom: 15px;
            font-size: 1.3em;
        }}
        .greeting {{
            font-size: 1.1em;
            margin-bottom: 20px;
            color: #555;
        }}
        .item {{
            margin-bottom: 20px;
            padding-left: 10px;
            border-left: 3px solid #667eea;
        }}
        .item-title {{
            font-weight: 600;
            color: #333;
            margin-bottom: 5px;
        }}
        .item-description {{
            color: #555;
            margin-bottom: 5px;
        }}
        .item-source {{
            font-size: 0.9em;
            color: #667eea;
        }}
        .item-source a {{
            color: #667eea;
            text-decoration: none;
        }}
        .item-source a:hover {{
            text-decoration: underline;
        }}
        .footer {{
            margin-top: 40px;
            padding-top: 20px;
            border-top: 1px solid #ddd;
            text-align: center;
            color: #888;
            font-size: 0.9em;
        }}
        .category-count {{
            color: #888;
            font-size: 0.9em;
            font-style: italic;
        }}
    </style>
</head>
<body>
    <div class="container">
{body_content}
    </div>
</body>
</html>"""

def save_digest(html_content):
    """Save digest to latest_digest.html"""
    output_path = SCRIPT_DIR / "latest_digest.html"

    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(html_content)
        log(f"✓ Digest saved to {output_path}")
        return True
    except Exception as e:
        log(f"Error saving digest: {e}")
        return False

def main():
    """Main function"""
    try:
        log("=" * 60)
        log("Automated Intranet Weekly Digest Generator")
        log("=" * 60)

        # Load configuration
        log("\nLoading API configuration...")
        config = load_config()
        log("✓ Configuration loaded")

        # Perform searches
        search_results = perform_searches(config)
        total_results = sum(len(results) for results in search_results.values())
        log(f"\n✓ Completed all searches ({total_results} total results)")

        # Generate digest with Claude
        log("\nGenerating digest with Claude API...")
        digest_body = generate_digest_with_claude(search_results, config)

        # Wrap in full HTML
        full_html = wrap_html(digest_body)

        # Save digest
        log("\nSaving digest...")
        if save_digest(full_html):
            log("\n" + "=" * 60)
            log("SUCCESS! Digest generated and saved")
            log("=" * 60)
            log("\nNext step: Automated email will be sent at scheduled time")
            return 0
        else:
            log("\n" + "=" * 60)
            log("ERROR: Failed to save digest")
            log("=" * 60)
            return 1

    except Exception as e:
        log(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
        return 1

if __name__ == "__main__":
    exit(main())
