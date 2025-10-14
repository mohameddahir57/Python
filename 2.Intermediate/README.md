# **Python Fundamentals: A Intermediate Guide** 
Excellent ✅ Perfect — we’ll keep the exact same structure and style as your beginner `README.md` (clear explanations + code examples + notes).


### 🟡 Intermediate Level (Days 11–20)

| Day | Topic                                                    |
| --- | -------------------------------------------------------- |
| 11  | Advanced Data Structures (Nested lists, dicts, and sets) |
| 12  | Advanced Functions (*args, **kwargs, recursion, scope)   |
| 13  | Modules and Packages (creating and importing)            |
| 14  | File Handling (CSV, JSON, working with structured data)  |
| 15  | Error Handling & Debugging (custom exceptions, logging)  |
| 16  | Regular Expressions (pattern matching with `re`)         |
| 17  | List/Dict Comprehensions and Generators                  |
| 18  | Working with APIs (using `requests` and JSON)            |
| 19  | Dates & Times (datetime module, formatting, timedelta)   |
| 20  | Mini Project – Command Line Tool or Data Script          |

## **Day 11 — Advanced Data Structures (nested lists, nested dicts, sets of tuples)**

**Explanation**
You already know lists, dicts, sets and tuples. Now we use them together: nested structures let you store complex data (like records, matrices, graphs). Learn how to index, iterate, and modify nested structures safely.

**Example**

```python
# Nested list: matrix (3x3)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Access element (row 2, col 1) -> 5
print(matrix[1][1])

# Nested dict: user records
users = {
    "alice": {"age": 30, "email": "alice@example.com"},
    "bob":   {"age": 25, "email": "bob@site.com"}
}

# Read Bob's email
print(users["bob"]["email"])

# Set of tuples for unique coordinate points
points = {(0, 0), (1, 2), (0, 0)}  # duplicate removed
print(points)
```

**Notes / Exercises**

* Exercise: Given a matrix, write a function to compute the transpose.
* Exercise: Safely get a user's phone number from nested dict using `.get()` with defaults.
* Be careful with mutable defaults and shallow copies when copying nested structures.

---

## **Day 12 — Advanced Functions (`*args`, `**kwargs`, recursion, scope, closures)**

**Explanation**
Learn flexible argument handling (`*args`, `**kwargs`), recursion for divide-and-conquer problems, scope rules (local/global), and closures (functions that remember state).

**Example**

```python
# *args and **kwargs
def printer(*args, **kwargs):
    print("args:", args)
    print("kwargs:", kwargs)

printer(1, 2, name="Alice", city="Hargeisa")

# Recursion: factorial
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))  # 120

# Closure: counter
def make_counter():
    count = 0
    def inc():
        nonlocal count
        count += 1
        return count
    return inc

c = make_counter()
print(c(), c(), c())  # 1 2 3
```

**Notes / Exercises**

* Exercise: Write a recursive function for Fibonacci (and then optimize with memoization).
* Remember recursion depth limits; Python default recursion limit ~1000.
* Practice using closures to hide internal data instead of global variables.

---

## **Day 13 — Modules & Packages (creating, importing, `__init__`)**

**Explanation**
Split code into modules (files) and packages (folders with `__init__.py`). Use imports to reuse code. Learn relative imports and best practices for project structure.

**Example**

```python
# Suppose project structure:
# myproj/
#   ├─ utils/
#   │   ├─ __init__.py
#   │   └─ math_utils.py
#   └─ main.py

# math_utils.py
def add(a, b):
    return a + b

# main.py
from utils.math_utils import add

print(add(3, 4))  # 7
```

**Notes / Exercises**

* Exercise: Create a small package `texttools` with functions `count_words()` and `is_palindrome()`.
* Use `if __name__ == "__main__":` for test code in modules.
* Avoid circular imports by organizing helpers into separate modules.

---

## **Day 14 — File Handling: CSV & JSON (structured data)**

**Explanation**
Work with common data formats: CSV (comma-separated values) and JSON (nested data). Use `csv` and `json` modules to read/write structured data.

**Example**

```python
import csv
import json

# Write CSV
rows = [["name", "age"], ["Alice", 30], ["Bob", 25]]
with open("people.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(rows)

# Read CSV
with open("people.csv", "r", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row["name"], row["age"])

# JSON: write and read
data = {"users": [{"name": "Alice", "id": 1}, {"name": "Bob", "id": 2}]}
with open("data.json", "w") as f:
    json.dump(data, f, indent=2)

with open("data.json", "r") as f:
    loaded = json.load(f)
    print(loaded["users"][0]["name"])
```

**Notes / Exercises**

* Exercise: Convert a CSV file to JSON.
* Pay attention to character encodings (use `encoding="utf-8"` when needed).
* Use `with` to safely open files.

---

## **Day 15 — Error Handling & Debugging (custom exceptions, logging)**

**Explanation**
Use `try/except` for robust programs. Create custom exception classes and use `logging` instead of many `print()` statements for scalable debugging and production-ready apps.

**Example**

```python
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(levelname)s:%(message)s")

class NegativeNumberError(Exception):
    pass

def sqrt(n):
    if n < 0:
        raise NegativeNumberError("Cannot take sqrt of negative number.")
    return n ** 0.5

try:
    print(sqrt(-5))
except NegativeNumberError as e:
    logging.error("Error computing sqrt: %s", e)
```

**Notes / Exercises**

* Exercise: Add logging to a script and log at DEBUG/INFO/WARNING/ERROR levels.
* Exercise: Create a function that raises a custom exception when input is invalid.
* Use `traceback` or an IDE debugger for stack traces.

---

## **Day 16 — Regular Expressions (`re`): pattern matching & extraction**

**Explanation**
Regular expressions let you search and extract patterns from text (emails, phone numbers, tokens). Learn `re.search`, `re.match`, `re.findall`, and `re.sub`.

**Example**

```python
import re

text = "Contact: alice@example.com or bob123@site.co.uk"
emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)
print(emails)

# Replace all digits with '#'
print(re.sub(r"\d", "#", "Phone: 123-456-7890"))
```

**Notes / Exercises**

* Exercise: Validate a simple phone number format with regex.
* Remember to use raw strings `r"pattern"` to avoid escaping backslashes.
* Test regex with online testers or small scripts.

---

## **Day 17 — Comprehensions & Generators (efficient loops, `yield`)**

**Explanation**
Comprehensions create lists/dicts/sets succinctly. Generators produce values lazily with `yield` (good for large data streams).

**Example**

```python
# List comprehension
squares = [x*x for x in range(10) if x % 2 == 0]
print(squares)

# Dict comprehension
names = ["alice", "bob"]
id_map = {name: idx for idx, name in enumerate(names)}
print(id_map)

# Generator function
def countdown(n):
    while n > 0:
        yield n
        n -= 1

for num in countdown(5):
    print(num)
```

**Notes / Exercises**

* Exercise: Convert a function that returns a list into a generator to save memory.
* Use generator expressions `(x*x for x in range(...))` when you don't need a list.
* Understand one-time-use nature of generators (after exhausted, must recreate).

---

## **Day 18 — Working with APIs (`requests`, JSON handling)**

**Explanation**
APIs let your program talk to services. Use `requests` to send HTTP requests and parse JSON responses. (Install with `pip install requests`.)

**Example**

```python
# Requires 'requests' package
import requests

url = "https://api.agify.io"  # free sample API
params = {"name": "mohamed"}
resp = requests.get(url, params=params)

if resp.status_code == 200:
    data = resp.json()
    print(data)  # example: {'name': 'mohamed', 'age': 28, 'count': 1234}
else:
    print("Request failed:", resp.status_code)
```

**Notes / Exercises**

* Exercise: Call a public API, parse JSON, and save results to a file.
* Always check `resp.status_code` and handle network errors with `try/except`.
* Beware of API rate limits and include headers when needed.

---

## **Day 19 — Dates & Times (`datetime`, `time`, formatting)**

**Explanation**
Work with date and time using `datetime` and `timedelta`. Parse/format dates and do date arithmetic.

**Example**

```python
from datetime import datetime, timedelta

now = datetime.now()
print("Now:", now)

# Formatting
print(now.strftime("%Y-%m-%d %H:%M:%S"))

# Parse string to datetime
s = "2025-10-14 19:00:00"
dt = datetime.strptime(s, "%Y-%m-%d %H:%M:%S")
print("Parsed:", dt)

# Add 7 days
future = now + timedelta(days=7)
print("One week later:", future)
```

**Notes / Exercises**

* Exercise: Calculate days until a given birthday.
* Be careful with timezones — for advanced timezone handling use `pytz` or `zoneinfo` (Python 3.9+).
* Use ISO 8601 format for portability.

---

## **Day 20 — Mini Project: Command-Line Tool (combine topics)**

**Explanation**
Build a small CLI tool to solidify what you learned. Example: a “contacts manager” that stores contacts in JSON, supports add/list/search, and uses logging and exceptions.

**Example (simple CLI starter)**

```python
# contacts_cli.py
import json
import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
DATA_FILE = Path("contacts.json")

def load_contacts():
    if DATA_FILE.exists():
        return json.loads(DATA_FILE.read_text())
    return {}

def save_contacts(contacts):
    DATA_FILE.write_text(json.dumps(contacts, indent=2))

def add_contact(name, phone):
    contacts = load_contacts()
    if name in contacts:
        logging.warning("Contact already exists.")
        return
    contacts[name] = {"phone": phone}
    save_contacts(contacts)
    logging.info("Contact added.")

def list_contacts():
    contacts = load_contacts()
    for name, info in contacts.items():
        print(name, info["phone"])

if __name__ == "__main__":
    # Simple test run
    add_contact("Alice", "123-456")
    add_contact("Bob", "555-000")
    list_contacts()
```






