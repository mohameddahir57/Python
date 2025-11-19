"""
file_utils.py - utility functions for working with CSV, Excel, PDF, and images.
"""
import csv
from pathlib import Path

# CSV
def csv_stats(path):
    path = Path(path)
    numbers = []
    with path.open("r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                numbers.append(float(row.get("value", 0)))
            except ValueError:
                continue
    if not numbers:
        return {"count":0}
    return {
        "count": len(numbers),
        "min": min(numbers),
        "max": max(numbers),
        "sum": sum(numbers),
        "average": sum(numbers)/len(numbers),
    }

# Excel
def excel_stats(path):
    try:
        import pandas as pd
    except ImportError:
        raise RuntimeError("pandas is required to read Excel files. Install with 'pip install pandas openpyxl'")
    df = pd.read_excel(path)
    # expect a 'value' column
    if "value" not in df.columns:
        return {"error": "No 'value' column found"}
    series = pd.to_numeric(df["value"], errors="coerce").dropna()
    if series.empty:
        return {"count":0}
    return {
        "count": int(series.count()),
        "min": float(series.min()),
        "max": float(series.max()),
        "sum": float(series.sum()),
        "average": float(series.mean()),
    }

# PDF
def extract_pdf_text(path):
    try:
        from PyPDF2 import PdfReader
    except ImportError:
        raise RuntimeError("PyPDF2 is required to read PDF files. Install with 'pip install PyPDF2'")
    reader = PdfReader(path)
    text = []
    for page in reader.pages:
        text.append(page.extract_text() or "")
    return "\n".join(text)

# Image
def image_info(path):
    try:
        from PIL import Image
    except ImportError:
        raise RuntimeError("Pillow is required for image operations. Install with 'pip install Pillow'")
    with Image.open(path) as im:
        return {
            "format": im.format,
            "mode": im.mode,
            "size": im.size,
        }
