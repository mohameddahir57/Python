# **Python Fundamentals: Advanced Guide** 

### 🔵 Advanced Level (Days 21–30)

| Day | Topic                                                 |
| --- | ----------------------------------------------------- |
| 21  | Advanced OOP (inheritance, polymorphism, decorators)  |
| 22  | Functional Programming (map, filter, reduce, lambda)  |
| 23  | Decorators & Context Managers                         |
| 24  | Iterators and Generators (custom classes, `__iter__`) |
| 25  | Working with Databases (SQLite CRUD)                  |
| 26  | Web Scraping (requests + BeautifulSoup)               |
| 27  | Automation with Python (scripts, scheduling)          |
| 28  | Unit Testing (`unittest` and `pytest`)                |
| 29  | File Handling Advanced (PDF, Excel, image files)      |
| 30  | Final Project – Real-World Python Application         |



### **Day 21: Advanced OOP (Inheritance, Polymorphism, Decorators)**

#### **1. Inheritance**

Inheritance allows a class to **reuse methods and attributes** from another class.

* **Parent class (Base)** → contains common features
* **Child class (Derived)** → inherits from parent, can add/override features

**Example:**

```python
# Parent class
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print(f"{self.name} makes a sound.")

# Child class
class Dog(Animal):
    def speak(self):
        print(f"{self.name} says Woof!")

# Usage
a = Animal("Generic Animal")
a.speak()  # Generic Animal makes a sound.

d = Dog("Buddy")
d.speak()  # Buddy says Woof!
```

**Tip:** Use `super().__init__()` in child classes to call the parent constructor.

---

#### **2. Polymorphism**

Polymorphism allows different objects to **use the same interface** but behave differently.

* Useful for **flexible code** where objects can be used interchangeably.

**Example:**

```python
class Cat(Animal):
    def speak(self):
        print(f"{self.name} says Meow!")

# Function using polymorphism
def animal_speak(animal):
    animal.speak()

animals = [Dog("Buddy"), Cat("Kitty"), Animal("Generic")]
for a in animals:
    animal_speak(a)
```

**Tip:** Polymorphism shines when working with collections of mixed objects.

---

#### **3. Decorators in OOP**

Decorators allow you to **modify or enhance functions/methods** without changing their code.

* Common in OOP for logging, access control, timing, etc.

**Example:**

```python
def uppercase_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper

class Greeter:
    @uppercase_decorator
    def greet(self, name):
        return f"Hello, {name}"

g = Greeter()
print(g.greet("Alice"))  # HELLO, ALICE
```

**Extra Info:**

* You can decorate class methods or even entire classes.
* `@staticmethod` and `@classmethod` are special built-in decorators in Python.

---

## **Day 22: Functional Programming (map, filter, reduce, lambda)**

**1. Lambda Functions**
Anonymous, short functions defined with `lambda`.

```python
square = lambda x: x ** 2
print(square(5))  # 25
```

**2. Map**
Applies a function to all items in a list.

```python
numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x**2, numbers))
print(squared)  # [1, 4, 9, 16]
```

**3. Filter**
Filters items based on a condition.

```python
numbers = [1, 2, 3, 4, 5]
even = list(filter(lambda x: x % 2 == 0, numbers))
print(even)  # [2, 4]
```

**4. Reduce**
Reduces a list to a single value (needs `functools.reduce`).

```python
from functools import reduce
numbers = [1, 2, 3, 4]
sum_all = reduce(lambda x, y: x + y, numbers)
print(sum_all)  # 10
```

**Tip:** Functional programming is great for **clean, concise, and immutable code**.

---

## **Day 23: Decorators & Context Managers**

**1. Decorators (Review + Advanced)**

```python
def timer(func):
    import time
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Execution time: {end-start:.4f} seconds")
        return result
    return wrapper

@timer
def compute():
    sum([i**2 for i in range(100000)])
    
compute()
```

**2. Context Managers (`with` statement)**
Used to **manage resources** (files, network, DB) safely.

```python
with open("example.txt", "w") as f:
    f.write("Hello World!")
# File automatically closed here
```

**Custom Context Manager Example:**

```python
class Managed:
    def __enter__(self):
        print("Start")
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("End")

with Managed():
    print("Inside block")
```

**Tip:** Use context managers to **avoid forgetting cleanup** like closing files or connections.

---

## **Day 24: Iterators and Generators**

**1. Iterators**
Objects you can loop over using `iter()` and `next()`.

```python
numbers = [1, 2, 3]
it = iter(numbers)
print(next(it))  # 1
print(next(it))  # 2
```

**2. Generators**
Functions that yield values **lazily**, saving memory.

```python
def squares(n):
    for i in range(n):
        yield i**2

for x in squares(5):
    print(x)
```

**3. Custom Iterator Class**

```python
class MyRange:
    def __init__(self, limit):
        self.limit = limit
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.limit:
            self.current += 1
            return self.current - 1
        else:
            raise StopIteration

for i in MyRange(5):
    print(i)
```

**Tip:** Generators are perfect for **large data streams**.

---

## **Day 25: Working with Databases (SQLite CRUD)**

```python
import sqlite3

# Connect / Create database
conn = sqlite3.connect("test.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER
)
""")

# Insert
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Alice", 25))
conn.commit()

# Read
cursor.execute("SELECT * FROM users")
print(cursor.fetchall())

# Update
cursor.execute("UPDATE users SET age=? WHERE name=?", (26, "Alice"))
conn.commit()

# Delete
cursor.execute("DELETE FROM users WHERE name=?", ("Alice",))
conn.commit()

conn.close()
```

**Tip:** Always use parameterized queries (`?`) to **prevent SQL injection**.

---

## **Day 26: Web Scraping (requests + BeautifulSoup)**

```python
import requests
from bs4 import BeautifulSoup

url = "https://example.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Extract title
title = soup.title.text
print(title)

# Extract all links
links = [a['href'] for a in soup.find_all('a', href=True)]
print(links)
```

**Tip:**

* Check `robots.txt` before scraping.
* Use headers to mimic a browser.

---

## **Day 27: Automation with Python (scripts, scheduling)**

**1. Automate file operations**

```python
import os, shutil

# Move files
shutil.move("source.txt", "destination.txt")
```

**2. Automate repetitive tasks with `schedule`**

```python
import schedule
import time

def job():
    print("Running task...")

schedule.every(5).seconds.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
```

**Tip:** Automation is powerful for **daily tasks, data collection, or notifications**.

---

## **Day 28: Unit Testing (`unittest` and `pytest`)**

**1. Using `unittest`**

```python
import unittest

def add(a, b):
    return a + b

class TestMath(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2,3), 5)
        self.assertNotEqual(add(2,2), 5)

if __name__ == "__main__":
    unittest.main()
```

**2. Using `pytest` (simpler syntax)**

```python
def add(a,b):
    return a+b

def test_add():
    assert add(2,3) == 5
```

**Tip:** Write tests to **catch bugs early** and **document expected behavior**.

---

## **Day 29: File Handling Advanced (PDF, Excel, Image Files)**

**1. PDF with `PyPDF2`**

```python
import PyPDF2

reader = PyPDF2.PdfReader("file.pdf")
print(reader.pages[0].extract_text())
```

**2. Excel with `openpyxl`**

```python
import openpyxl

wb = openpyxl.Workbook()
ws = wb.active
ws['A1'] = "Hello Excel"
wb.save("file.xlsx")
```

**3. Image with `Pillow`**

```python
from PIL import Image

img = Image.open("image.jpg")
img = img.resize((200, 200))
img.save("image_small.jpg")
```

**Tip:** Python can handle almost any file type—just choose the right library.

---

## **Day 30: Final Project – Real-World Python Application**

**Ideas for your final project:**

* **Mini Web Scraper** → collect news or weather data and save to Excel/DB.
* **Automated Report Generator** → read CSV/Excel, process data, create summary.
* **CLI Tool** → a command-line application that performs tasks like file management or reminders.
* **Simple Game** → text-based game using OOP and functions.

**Example Skeleton: Web Scraper + DB + CSV Output**

```python
import requests, sqlite3, csv
from bs4 import BeautifulSoup

# DB setup
conn = sqlite3.connect("data.db")
c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS articles(title TEXT, link TEXT)")

# Scrape
url = "https://example.com"
soup = BeautifulSoup(requests.get(url).text, "html.parser")
for a in soup.find_all('a', href=True):
    title = a.text
    link = a['href']
    c.execute("INSERT INTO articles (title, link) VALUES (?, ?)", (title, link))

conn.commit()

# Export CSV
with open("articles.csv", "w", newline="") as f:
    writer = csv.writer(f)
    for row in c.execute("SELECT * FROM articles"):
        writer.writerow(row)

conn.close()
```



