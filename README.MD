
### 1. 创建 Conda 环境

打开终端并创建一个新的 Conda 环境：

```bash
conda create -n ocr_env python=3.9
```

激活新创建的环境：

```bash
conda activate ocr_env
```

### 2. 创建 `requirements.txt` 文件

在项目目录下创建一个名为 `requirements.txt` 的文件，并将以下内容复制到其中：

```
pytesseract
pillow
pdf2image
python-docx
```

### 3. 安装依赖库

使用以下命令安装依赖库：

```bash
pip install -r requirements.txt
```

### 4. 安装 Tesseract OCR

使用 Homebrew 安装 Tesseract OCR：

```bash
brew install tesseract
brew install tesseract-lang
```

确保`TESSDATA_PREFIX`环境变量指向Tesseract的语言数据目录。你可以在终端中运行以下命令：

```
export TESSDATA_PREFIX=/usr/local/share/
```

### 5. 编写 OCR 脚本

在项目目录下创建一个名为 `pdf2docx.py` 的文件，并将以下内容复制到其中：

```python
import argparse
import pytesseract
from PIL import Image
from pdf2image import convert_from_path
from docx import Document
import os
from tkinter import Tk, filedialog
from tqdm import tqdm  # 导入 tqdm 库

# 设置 tesseract 路径
pytesseract.pytesseract.tesseract_cmd = '/usr/local/bin/tesseract'

# 确保 TESSDATA_PREFIX 环境变量设置正确
tessdata_dir = '/usr/local/share/tessdata'
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

```

### 6. 运行脚本

在包含 `pdf2docx.py` 和 `requirements.txt` 文件的目录中，使用以下命令运行脚本：

- OCR并输出为docx格式，使用中文和英文识别，通过命令行指定PDF文件：
  ```bash
  python pdf2docx.py -f path_to_file.pdf -o docx -l ce
  ```
- OCR并输出为txt格式，使用中文识别，通过命令行指定PDF文件：
  ```bash
  python pdf2docx.py -f path_to_file.pdf -o txt -l c
  ```
- OCR并输出为docx格式，使用默认的中文识别，通过图形界面选择PDF文件：
  ```bash
  python pdf2docx.py
  ```

这样，你就可以在macOS系统上使用这个脚本进行高质量的OCR，并输出为docx或txt格式，同时支持通过命令行指定PDF文件或通过图形界面选择PDF文件。