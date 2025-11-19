# File Handling Advanced (Day 29)
Project: File Handling Advanced — working with CSV, Excel, PDF, and image files.

## Overview
This mini-project demonstrates reading and writing common file types:
- CSV (`csv`)
- Excel (`openpyxl` / `pandas`)
- PDF (reading text from PDFs using `PyPDF2`)
- Images (basic operations with `Pillow`)

It provides:
- `file_utils.py`: functions for reading/writing and simple analysis.
- `main.py`: a small CLI to run utilities.
- `sample_data/`: sample CSV, XLSX, PDF, and PNG files.
- `tests/`: a simple unit test for some utilities.

## Requirements
See `requirements.txt`. Install with:

```bash
pip install -r requirements.txt
```

Default python: 3.11 (works with 3.8+).

## How to use
1. Install requirements.
2. Run the CLI:
```bash
python main.py --help
```
3. Examples:
```bash
python main.py stats --csv sample_data/data.csv
python main.py pdf-text --pdf sample_data/sample.pdf
python main.py image-info --image sample_data/image.png
```

## Deliverables
- `main.py`
- `file_utils.py`
- `requirements.txt`
- `README.md`
- sample files in `sample_data/`
- `tests/test_file_utils.py`

Enjoy! — Day 29
