#!/usr/bin/env python3
import requests
import sys
from bs4 import BeautifulSoup

def extract_links(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return []
    soup = BeautifulSoup(response.text, 'html.parser')
    links = [a['href'] for a in soup.find_all('a', href=True)]
    return links

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python link_extractor.py <URL>")
        sys.exit(1)
    url = sys.argv[1]
    links = extract_links(url)
    print(f"Found {len(links)} links:")
    for link in links:
        print(link)



