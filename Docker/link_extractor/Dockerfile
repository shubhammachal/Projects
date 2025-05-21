FROM python:3.11
LABEL maintainer="Shubham Machal"
LABEL description="Link Extractor for web pages"
WORKDIR /app
COPY requirements.txt link_extractor.py /app/

RUN pip install --no-cache-dir -r requirements.txt && \
    chmod +x /app/link_extractor.py
ENTRYPOINT ["python3", "/app/link_extractor.py"]