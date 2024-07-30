# PDF2TEXT (Simple Text Extractor)

A simple OCR script to convert PDF files to DOCX or TXT formats using Tesseract OCR. This script is designed to extract text without preserving the original formatting of the document.

## Getting Started

### 1. Clone the Repository

Clone the repository to your local machine:

```bash
git clone https://github.com/lancer1911/pdf2text.git
cd pdf2text
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

#### Windows

1. Download and install Tesseract OCR from [Tesseract at UB Mannheim](https://github.com/UB-Mannheim/tesseract/wiki).
2. Download and install Poppler from [Poppler for Windows](https://poppler.freedesktop.org/).
3. Add Tesseract and Poppler to your system PATH.
4. Ensure the `TESSDATA_PREFIX` environment variable points to the Tesseract language data directory. You can set it in your terminal:

```bash
setx TESSDATA_PREFIX "C:\Program Files\Tesseract-OCR\tessdata"
```

#### macOS

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

#### Linux

Install Tesseract OCR and Poppler using your package manager. For example, on Ubuntu:

```bash
sudo apt update
sudo apt install tesseract-ocr poppler-utils
```

To install additional language packs for Tesseract, you can use the following command:

```bash
sudo apt install tesseract-ocr-<language-code>
```

Replace `<language-code>` with the code for the language you want to install. Here are some examples:

- `eng` for English
- `chi-sim` for Simplified Chinese
- `chi-tra` for Traditional Chinese
- `deu` for German
- `jpn` for Japanese
- `fra` for French

To install multiple languages at once, you can use:

```bash
sudo apt install tesseract-ocr-eng tesseract-ocr-chi-sim tesseract-ocr-chi-tra tesseract-ocr-deu tesseract-ocr-jpn tesseract-ocr-fra
```

Ensure the `TESSDATA_PREFIX` environment variable points to the Tesseract language data directory. You can set it in your terminal:

```bash
export TESSDATA_PREFIX=/usr/share/tesseract-ocr/4.00/tessdata/
```

### 5. Run the Script

In the directory containing `pdf2text.py`, use the following commands to run the script:

- To perform OCR and output as DOCX format with Chinese and English recognition, specifying the PDF file through the command line:

  ```bash
  python pdf2text.py -f path_to_file.pdf -o docx -l ce
  ```

- To perform OCR and output as TXT format with Chinese recognition, specifying the PDF file through the command line:

  ```bash
  python pdf2text.py -f path_to_file.pdf -o txt -l c
  ```

- To perform OCR and output as DOCX format with default English recognition, using a GUI to select the PDF file:

  ```bash
  python pdf2text.py
  ```

## Script Overview

The script `pdf2text.py` performs the following steps:
1. Converts the PDF to images.
2. Applies OCR on each image using Tesseract.
3. Outputs the extracted text to either a DOCX or TXT file.

This script is intended for basic text extraction and does not retain the original formatting of the PDF.

## License

This project is licensed under the MIT License.
