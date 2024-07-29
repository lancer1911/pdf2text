# PDF2DOCX (Simple Text Extractor)

A simple OCR script to convert PDF files to DOCX or TXT formats using Tesseract OCR. This script is designed to extract text without preserving the original formatting of the document.

## Getting Started

### 1. Clone the Repository

Clone the repository to your local machine:

```bash
git clone https://github.com/lancer1911/pdf2docx.git
cd pdf2docx
```

Alternatively, you can download the ZIP file and extract it to your desired location.

### 2. Create Conda Environment

Open your terminal and create a new Conda environment:

```bash
conda create -n ocr_env python=3.9
```

Activate the newly created environment:

```bash
conda activate ocr_env
```

### 3. Install Dependencies

Install the required libraries using the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

### 4. Install Tesseract OCR and Poppler

Install Tesseract OCR and Poppler using Homebrew:

```bash
brew install tesseract
brew install tesseract-lang
brew install poppler
```

Ensure the `TESSDATA_PREFIX` environment variable points to the Tesseract language data directory. You can set it in your terminal:

```bash
export TESSDATA_PREFIX=/usr/local/share/
```

### 5. Run the Script

In the directory containing `pdf2docx.py` and `requirements.txt`, use the following commands to run the script:

- To perform OCR and output as DOCX format with Chinese and English recognition, specifying the PDF file through the command line:

  ```bash
  python pdf2docx.py -f path_to_file.pdf -o docx -l ce
  ```

- To perform OCR and output as TXT format with Chinese recognition, specifying the PDF file through the command line:

  ```bash
  python pdf2docx.py -f path_to_file.pdf -o txt -l c
  ```

- To perform OCR and output as DOCX format with default English recognition, using a GUI to select the PDF file:

  ```bash
  python pdf2docx.py
  ```

## Script Overview

The script `pdf2docx.py` performs the following steps:
1. Converts the PDF to images.
2. Applies OCR on each image using Tesseract.
3. Outputs the extracted text to either a DOCX or TXT file.

This script is intended for basic text extraction and does not retain the original formatting of the PDF.

## License

This project is licensed under the MIT License. 
