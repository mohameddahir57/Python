#!/usr/bin/env python3
"""
main.py - simple CLI for File Handling Advanced project
"""
import argparse
from file_utils import (
    csv_stats,
    excel_stats,
    extract_pdf_text,
    image_info,
)

def main():
    parser = argparse.ArgumentParser(description="File Handling Advanced CLI")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_stats = sub.add_parser("stats", help="Get stats from CSV or Excel")
    p_stats.add_argument("--csv", help="Path to CSV file")
    p_stats.add_argument("--excel", help="Path to Excel file")

    p_pdf = sub.add_parser("pdf-text", help="Extract text from PDF")
    p_pdf.add_argument("--pdf", required=True, help="Path to PDF file")

    p_img = sub.add_parser("image-info", help="Show basic image info")
    p_img.add_argument("--image", required=True, help="Path to image file")

    args = parser.parse_args()
    if args.cmd == "stats":
        if args.csv:
            print("CSV stats:")
            print(csv_stats(args.csv))
        if args.excel:
            print("Excel stats:")
            print(excel_stats(args.excel))
    elif args.cmd == "pdf-text":
        print("PDF text (first 500 chars):")
        print(extract_pdf_text(args.pdf)[:500])
    elif args.cmd == "image-info":
        print("Image info:")
        print(image_info(args.image))

if __name__ == "__main__":
    main()
