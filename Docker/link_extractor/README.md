# Link Extractor - Step 2

Enhanced link extraction module with full URI support and anchor text reporting.

## Features

- Normalizes relative paths to full URLs
- Extracts both links and anchor text
- Modular design for reuse in other scripts
- Dockerized for portability

## Files

- `Dockerfile` - Container configuration
- `link_extractor.py` - Enhanced Python script with modular functions
- `README.md` - This file

## Usage

### Build the Docker image:
```bash
docker image build -t link_extractor:step2 .
```

### Run the container:
```bash
docker container run -it --rm link_extractor:step2 <URL>
```

### Example:
```bash
docker container run -it --rm link_extractor:step2 https://example.com/
```

## Improvements from Step 1

- Full URL normalization using `urljoin()`
- Anchor text extraction and formatting
- Modular `extract_links()` function for reusability
- Better handling of image links with `[IMG]` placeholder