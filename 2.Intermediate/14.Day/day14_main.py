# Day 14 - File Handling (CSV, JSON, Structured Data)

import csv
import json

# --- Text File ---
with open("example.txt", "r") as file:
    print("TXT File Content:\n", file.read())

# --- CSV File ---
print("\nCSV File Content:")
with open("data.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# --- JSON File ---
print("\nJSON File Content:")
with open("person.json", "r") as file:
    data = json.load(file)
    print(data)

# --- Convert CSV to JSON ---
csv_data = []
with open("students.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        csv_data.append(row)
with open("students.json", "w") as file:
    json.dump(csv_data, file, indent=4)
print("\nCSV converted to students.json successfully!")
