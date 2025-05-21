#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import sys

def extract_links(url):
    """
    Fetch the page at the given URL and extract all anchor tags.
    Returns a list of tuples: (full_url, anchor_text)
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')
    result = []

    for a_tag in soup.find_all('a', href=True):
        href = urljoin(url, a_tag['href'])  # normalize to full URL
        text = a_tag.get_text(strip=True)  # get anchor text
        result.append((href, text))

    return result

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python link_extractor.py <URL>")
        sys.exit(1)

    url = sys.argv[1]
    links = extract_links(url)
    print(f"Found {len(links)} links:")
    for href, text in links:
        print(f"{href} (text: \"{text}\")")
