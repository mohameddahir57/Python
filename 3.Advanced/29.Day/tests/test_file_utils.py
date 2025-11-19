import os
from file_utils import csv_stats, excel_stats, image_info, extract_pdf_text

def test_csv_stats():
    data = {"count":7}
    res = csv_stats("sample_data/data.csv")
    assert res["count"] == 7

def test_excel_stats():
    res = excel_stats("sample_data/data.xlsx")
    assert res["count"] == 7

def test_image_info():
    info = image_info("sample_data/image.png")
    assert "size" in info

def test_pdf_text():
    txt = extract_pdf_text("sample_data/sample.pdf")
    assert len(txt) > 0
