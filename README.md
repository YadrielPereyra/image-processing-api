# Python Image Processing API + CLI Tool

## Description
A Python Flask REST API and Command-Line Interface (CLI) tool that allows users to upload, process, download, and delete images.  
This project simulates an enterprise-grade automation tool by converting uploaded images to grayscale, offering both API and CLI functionality, and is Dockerized for easy deployment.

---

## Features
- REST API (Flask)
- Command-Line Interface (CLI) using `argparse`
- Dockerized for production-ready deployment
- Supports:
  - Upload images
  - Auto-convert to grayscale
  - List processed images
  - Download processed images
  - Delete processed images

---

## Technologies Used
- Python 3.9+
- Flask
- Pillow (PIL)
- Requests
- Argparse
- Docker

---

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/YadrielPereyra/image-processing-api.git
cd image-processing-api

Install Dependencies
pip install -r requirements.txt

Run the API (Locally)
python app.py
API will be available at http://localhost:5000.

CLI Tool Usage (Locally)
python cli.py upload --file example.jpg

List processed images
python cli.py list

Download a processed image
python cli.py download --file example.jpg

Delete a processed image
python cli.py delete --file example.jpg

Author

Yadriel Pereyra

License

This project is licensed under the MIT License.
See the LICENSE file for details.

