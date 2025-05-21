# Docker Projects Collection 🐳

A collection of containerized applications and utilities built with Docker.

## 📋 Projects Overview

This repository contains multiple Docker projects, each demonstrating different containerization concepts and practical applications.

### 🔗 Step 1: Link Extractor

**Location:** `projects/docker/link_extractor` (branch: `step1`)

A simple containerized Python script that extracts all hyperlinks from web pages.

**Features:**
- Web scraping with BeautifulSoup4 and Requests
- Containerized Python application
- Command-line interface
- Easy deployment with Docker

**Quick Usage:**
```bash
# Navigate to the project
git checkout step1
cd projects/docker/link_extractor

# Build the image
docker build -t link_extractor .

# Run the container
docker run link_extractor https://example.com
```

**Docker Hub:** `smachal2322/link_extractor:step1`

---

## 🚀 Getting Started

### Prerequisites
- Docker installed on your system
- Git for cloning the repository

### Repository Structure
```
├── README.md                           # This file
├── projects/
│   └── docker/
│       └── link_extractor/            # Step 1 project
│           ├── Dockerfile
│           ├── linkextractor.py
│           └── README.md
└── [future projects will be added here]
```

### Exploring Projects

Each project is organized in its own branch for better version control:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/shubhammachal/Projects.git
   cd Docker
   ```

2. **Switch to a specific project branch:**
   ```bash
   git checkout step1  # For link extractor project
   ```

3. **Follow the project-specific README in each branch**

## 🎯 Project Goals

This repository aims to:
- Demonstrate various Docker containerization patterns
- Provide practical, real-world Docker examples
- Show progression from simple to complex containerized applications
- Serve as a learning resource for Docker best practices

## 📚 Learning Path

- **Step 1** - Basic containerization with Python web scraping tool
- **Step 2** - Coming soon...
- **Step 3** - Coming soon...

## 🛠️ Technologies Used

- ![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=flat&logo=docker&logoColor=white) Docker
- ![Python](https://img.shields.io/badge/python-3670A0?style=flat&logo=python&logoColor=white) Python
- Various other technologies per project

## 🤝 Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 👨‍💻 Author

**Shubham Machal**
- GitHub: [@shubhammachal](https://github.com/shubhammachal)
- Docker Hub: [smachal2322](https://hub.docker.com/u/smachal2322)

---

⭐ **Star this repository if you find it helpful!**
