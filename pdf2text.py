import argparse
import pytesseract
from PIL import Image
from pdf2image import convert_from_path
from docx import Document
import os
from tkinter import Tk, filedialog
from tqdm import tqdm

def set_tesseract_path():
    if os.name == 'nt':  # Windows
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
        tessdata_dir = r'C:\Program Files\Tesseract-OCR\tessdata'
    elif os.name == 'posix':  # macOS and Linux
        pytesseract.pytesseract.tesseract_cmd = '/usr/local/bin/tesseract'
        tessdata_dir = '/usr/local/share/tessdata'
    else:
        raise OSError("Unsupported operating system.")
    
    if not os.path.exists(tessdata_dir):
        raise FileNotFoundError(f"Tessdata directory not found: {tessdata_dir}")

    os.environ['TESSDATA_PREFIX'] = tessdata_dir

def pdf_to_images(pdf_path):
    try:
        return convert_from_path(pdf_path)
    except Exception as e:
        print(f"Error converting PDF to images: {e}")
        return []

def ocr_to_docx(images, lang, output_path):
    doc = Document()
    try:
        for img in tqdm(images, desc="Processing images to DOCX", bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt}"):
            text = pytesseract.image_to_string(img, lang=lang)
            for line in text.split('\n'):
                doc.add_paragraph(line)
        doc.save(output_path)
        print(f"Saved OCR result as DOCX at: {output_path}")
    except Exception as e:
        print(f"Error saving DOCX: {e}")

def ocr_to_txt(images, lang, output_path):
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            for img in tqdm(images, desc="Processing images to TXT", bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt}"):
                text = pytesseract.image_to_string(img, lang=lang)
                f.write(text + '\n')
        print(f"Saved OCR result as TXT at: {output_path}")
    except Exception as e:
        print(f"Error saving TXT: {e}")

def get_pdf_file():
    root = Tk()
    root.withdraw()  # 隐藏根窗口
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    return file_path

def parse_language(lang_input):
    lang_dict = {
        'c': 'chi_sim',
        'e': 'eng',
        'g': 'deu',
        'j': 'jpn',
        'f': 'fra'
    }
    lang = ''.join([lang_dict[l] for l in lang_input if l in lang_dict])
    if not lang:
        raise ValueError(f"Invalid language code provided: {lang_input}")
    return lang

def main():
    parser = argparse.ArgumentParser(description="Perform OCR on a PDF and output as DOCX or TXT.")
    parser.add_argument('-f', '--file', help="Path to the PDF file for OCR")
    parser.add_argument('-o', '--output', choices=['docx', 'txt'], default='docx', help="Output format (docx or txt)")
    parser.add_argument('-l', '--language', default='e', help="Language for OCR: -l:c for Chinese, -l:e for English, -l:g for German, -l:j for Japanese, -l:f for French. Combine languages with -l:ce for Chinese and English")

    args = parser.parse_args()

    set_tesseract_path()

    if args.file:
        pdf_file = args.file
    else:
        pdf_file = get_pdf_file()

    if not pdf_file:
        print("No PDF file selected. Exiting.")
        return

    try:
        lang = parse_language(args.language)
    except ValueError as e:
        print(e)
        return

    images = pdf_to_images(pdf_file)
    if not images:
        print("No images extracted from PDF. Exiting.")
        return

    output_path = os.path.splitext(pdf_file)[0] + '.' + args.output

    if args.output == 'docx':
        ocr_to_docx(images, lang, output_path)
    elif args.output == 'txt':
        ocr_to_txt(images, lang, output_path)

if __name__ == "__main__":
    main()
