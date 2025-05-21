# Containerized Link Extractor 🔗

[![Docker Pulls](https://img.shields.io/docker/pulls/smachal2322/link_extractor.svg)](https://hub.docker.com/r/smachal2322/link_extractor)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A simple, containerized Python script that extracts links from web pages.

## 📖 Description

This container provides a utility to extract all links from a specified website URL. The script uses Python's BeautifulSoup4 and Requests libraries to fetch and parse HTML content, extracting all hyperlinks found on the page.

## 🛠️ Technology Stack

- ![Python](https://img.shields.io/badge/python-3670A0?style=flat&logo=python&logoColor=white) Python 3
- BeautifulSoup4
- Requests
- ![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=flat&logo=docker&logoColor=white) Docker

## 🐳 Docker Image

The Docker image is available on Docker Hub:

```bash
docker pull smachal2322/link_extractor:step1
```

## 📋 Usage

### Basic Usage

```bash
docker run smachal2322/link_extractor:step1 https://example.com
```

This will extract all links from example.com and print them to standard output.

### Output to File

```bash
docker run smachal2322/link_extractor:step1 https://example.com > links.txt
```

This will save all extracted links to a file named `links.txt`.

## 📝 Dockerfile

```dockerfile
FROM       python:3
LABEL      maintainer="Shubham Machal <@smachal2322>"
RUN        pip install beautifulsoup4
RUN        pip install requests
WORKDIR    /app
COPY       linkextractor.py /app/
RUN        chmod a+x linkextractor.py
ENTRYPOINT ["./linkextractor.py"]
```

## 🔍 Script Details

The container runs `link_extractor.py`, which:

1. Accepts a URL as a command-line argument
2. Fetches the web page at the specified URL
3. Parses the HTML content
4. Extracts all hyperlinks (`<a>` tags with `href` attributes)
5. Prints the links to standard output

## 🏗️ Building the Image Locally

If you want to build the image locally:

```bash
# Clone this repository
git clone https://github.com/shubhammachal/Projects
cd Docker/link_extractor

# Build the Docker image
docker build -t link_extractor:step1 .
```

## 🚀 Quick Start

```bash
# Pull the image
docker pull smachal2322/link_extractor:step1

# Run the container
docker run smachal2322/link_extractor:step1 https://github.com
```

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 👨‍💻 Maintainer

Maintained by Shubham Machal ([@shubhammachal](https://github.com/shubhammachal)).

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
