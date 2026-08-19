#!/usr/bin/env python3
"""
ocr_book.py — Extract text from scanned PDFs and images.

Usage:
    python scripts/ocr_book.py raw/books/my-book/book.pdf --lang ara+deu --output raw/books/my-book/my-book-extracted.txt

This script:
- Converts PDF to images (one per page)
- Runs Tesseract OCR with specified language(s)
- Outputs page-by-page text to a single file with page markers
- Works with Arabic, German, English, and mixed-language books.
"""

import argparse
import os
import sys
import subprocess
import tempfile


def check_dependency(name, cmd, install_hint=None):
    try:
        subprocess.run(
            [cmd, "--version"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            timeout=5,
            check=True,
        )
        print(f"[OK] {name} found.")
        return True
    except (subprocess.TimeoutExpired, subprocess.CalledProcessError, FileNotFoundError):
        # Try known Windows path for Tesseract
        if name == "Tesseract OCR" and sys.platform == "win32":
            tess_path = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
            if os.path.exists(tess_path):
                print(f"[OK] {name} found at {tess_path}.")
                os.environ["TESSERACT_CMD"] = tess_path
                return True
        print(f"[MISSING] {name} not found.")
        if install_hint:
            print(f"  Install: {install_hint}")
        sys.exit(1)


def pdf_to_images(pdf_path, dpi=300):
    """Use pdftoppm to convert PDF to PNG images (one per page)."""
    check_dependency("pdftoppm (poppler-utils)", "pdftoppm")
    with tempfile.TemporaryDirectory() as tmpdir:
        prefix = os.path.join(tmpdir, "page")
        subprocess.run(
            [
                "pdftoppm",
                "-png",
                "-r",
                str(dpi),
                pdf_path,
                prefix,
            ],
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        images = sorted(f for f in os.listdir(tmpdir) if f.endswith(".png"))
        paths = [os.path.join(tmpdir, img) for img in images]
        print(f"[INFO] Converted PDF to {len(paths)} pages.")
        return paths


def ocr_image(image_path, lang="ara+deu"):
    """Run Tesseract OCR on a single image."""
    p = subprocess.run(
        ["tesseract", image_path, "stdout", "-l", lang],
        capture_output=True,
        text=True,
        timeout=60,
    )
    if p.returncode != 0:
        print(f"[WARN] OCR error on {image_path}: {p.stderr.strip()}")
        return ""
    return p.stdout.strip()


def ocr_book(input_path, lang="ara+deu"):
    """OCR an entire PDF and return page-by-page text."""
    if input_path.lower().endswith(".pdf"):
        images = pdf_to_images(input_path)
    elif input_path.lower().endswith((".png", ".jpg", ".jpeg", ".tiff")):
        images = [input_path]
    else:
        print(f"[ERROR] Unsupported file type: {input_path}")
        sys.exit(1)

    pages = []
    for i, img in enumerate(images, start=1):
        print(f"[OCR] Page {i}/{len(images)}...")
        text = ocr_image(img, lang=lang)
        pages.append((i, text))
    return pages


def save_pages(pages, output_path):
    """Save page-by-page text with markers."""
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        for page_num, text in pages:
            f.write(f"\n=== PAGE {page_num} ===\n\n{text}\n\n")
    print(f"[DONE] Saved {len(pages)} pages to {output_path}")


def main():
    parser = argparse.ArgumentParser(description="OCR scanned book (PDF or image)")
    parser.add_argument("input", help="Path to PDF or image file")
    parser.add_argument(
        "--lang",
        default="ara+deu",
        help="Tesseract language(s), e.g. 'ara', 'deu', 'eng', 'ara+deu', 'ara+eng'",
    )
    parser.add_argument(
        "--output",
        required=True,
        help="Path to save extracted text",
    )
    parser.add_argument(
        "--dpi",
        type=int,
        default=300,
        help="Scan resolution for PDF conversion (default: 300)",
    )
    args = parser.parse_args()

    print("[CHECK] Verifying dependencies...")
    check_dependency(
        "Tesseract OCR",
        "tesseract",
        "On Windows: install via choco install tesseract-ocr or from https://github.com/UB-Mannheim/tesseract/wiki",
    )

    print(f"[INFO] Running OCR on {args.input} with lang={args.lang}")
    pages = ocr_book(args.input, lang=args.lang)
    save_pages(pages, args.output)


if __name__ == "__main__":
    main()
