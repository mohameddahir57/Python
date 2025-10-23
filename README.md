# 30 Days of Python: Complete Learning Journey

Welcome to your **30-Day Python Learning Plan**, designed to take you from beginner to advanced level. This comprehensive guide combines all your progress from three phases:

- **Beginner (Days 1–10)** – Python basics, syntax, control flow, and OOP fundamentals.  
- **Intermediate (Days 11–20)** – Advanced functions, regex, APIs, comprehensions, and practical projects.  
- **Advanced (Days 21–30)** – Advanced OOP, databases, web scraping, automation, and final projects.

Each day includes explanations, code examples, and exercises to reinforce understanding.

---

## 🟢 Phase 1: Beginner (Days 1–10)

### Day 1 — Introduction to Python
- Understand what Python is and where it’s used.
- Learn about interpreters and compilers.

```python
print("Hello, World!")
```

---

### Day 2 — Installing Python & Setting Up Environment
- Install Python and set up VS Code or Jupyter Notebook.
- Learn about virtual environments and `pip`.

```bash
python -m venv myenv
source myenv/bin/activate  # macOS/Linux
myenv\Scripts\activate     # Windows
```

---

### Day 3 — Basic Syntax & Variables
- Learn data types (int, float, str, bool).
- Explore variable naming rules.

```python
a = 5
pi = 3.14
name = "Amin"
is_valid = True
```

---

### Day 4 — Operators
- Arithmetic, comparison, logical, and assignment operators.

```python
x, y = 10, 3
print(x + y, x // y, x % y)
```

---

### Day 5 — Control Flow
- Practice `if/elif/else`, `for`, and `while` loops.

```python
age = 20
if age < 18:
    print("Minor")
else:
    print("Adult")
```

---

### Day 6 — Data Structures
- Lists, tuples, sets, dictionaries.

```python
fruits = ["apple", "banana", "cherry"]
print(fruits[0])
```

---

### Day 7 — String Manipulation
- f-strings, `.split()`, `.upper()`, `.lower()`.

```python
name = "Amin"
print(f"Hello, {name.upper()}!")
```

---

### Day 8 — Functions & Modules
- Define, call, and import functions.

```python
def greet(name):
    return f"Hello, {name}!"
print(greet("Amin"))
```

---

### Day 9 — File I/O & Exceptions
- Read/write files and use `try/except`.

```python
try:
    with open("data.txt", "w") as f:
        f.write("Hello!")
except Exception as e:
    print("Error:", e)
```

---

### Day 10 — Object-Oriented Programming (OOP)
- Classes, objects, and inheritance.

```python
class Car:
    def __init__(self, brand):
        self.brand = brand

    def drive(self):
        print(f"{self.brand} is moving!")

my_car = Car("Toyota")
my_car.drive()
```

---

## 🟡 Phase 2: Intermediate (Days 11–20)

### Day 11 — Advanced Data Structures
- Nested lists, dicts, and sets.

```python
users = {"Amin": {"age": 23, "city": "Hargeisa"}}
print(users["Amin"]["city"])
```

---

### Day 12 — Advanced Functions
- `*args`, `**kwargs`, recursion, and closures.

```python
def factorial(n):
    return 1 if n <= 1 else n * factorial(n-1)
```

---

### Day 13 — Modules & Packages
- Creating and importing your own modules.

```python
# math_utils.py
def add(a, b):
    return a + b
```

---

### Day 14 — File Handling: CSV & JSON

```python
import json
with open('data.json', 'w') as f:
    json.dump({"name": "Amin"}, f)
```

---

### Day 15 — Error Handling & Logging

```python
import logging
logging.basicConfig(level=logging.INFO)
try:
    1/0
except ZeroDivisionError:
    logging.error("Cannot divide by zero!")
```

---

### Day 16 — Regular Expressions

```python
import re
text = "Email: amin@example.com"
print(re.findall(r"[\w.-]+@[\w.-]+", text))
```

---

### Day 17 — Comprehensions & Generators

```python
squares = [x*x for x in range(10) if x % 2 == 0]
```

---

### Day 18 — Working with APIs

```python
import requests
resp = requests.get("https://api.agify.io?name=amin")
print(resp.json())
```

---

### Day 19 — Dates & Times

```python
from datetime import datetime, timedelta
print(datetime.now() + timedelta(days=5))
```

---

### Day 20 — Mini Project: CLI Contacts Manager

```python
import json
contacts = {"Amin": {"phone": "123-456"}}
json.dump(contacts, open("contacts.json", "w"))
```

---

## 🔵 Phase 3: Advanced (Days 21–30)

### Day 21 — Advanced OOP

```python
class Dog:
    def speak(self):
        print("Woof!")
```

---

### Day 22 — Functional Programming

```python
from functools import reduce
nums = [1,2,3]
print(reduce(lambda x,y: x+y, nums))
```

---

### Day 23 — Decorators & Context Managers

```python
def timer(func):
    import time
    def wrapper(*a, **kw):
        s=time.time(); func(); print(time.time()-s)
    return wrapper
```

---

### Day 24 — Iterators & Generators

```python
def countdown(n):
    while n>0:
        yield n; n-=1
```

---

### Day 25 — Databases (SQLite)

```python
import sqlite3
conn=sqlite3.connect('db.db')
conn.execute('CREATE TABLE IF NOT EXISTS users(name TEXT)')
```

---

### Day 26 — Web Scraping

```python
from bs4 import BeautifulSoup
import requests
html=requests.get('https://example.com').text
soup=BeautifulSoup(html,'html.parser')
print(soup.title.text)
```

---

### Day 27 — Automation with Python

```python
import schedule, time
schedule.every(5).seconds.do(lambda: print('Running...'))
while True:
    schedule.run_pending(); time.sleep(1)
```

---

### Day 28 — Unit Testing

```python
import unittest
class TestMath(unittest.TestCase):
    def test_add(self):
        self.assertEqual(2+3,5)
```

---

### Day 29 — File Handling Advanced

```python
from PIL import Image
img=Image.open('img.jpg')
img.resize((200,200)).save('new.jpg')
```

---

### Day 30 — Final Project
Combine everything: APIs, DBs, scraping, automation, and OOP.

---

## 🎯 Final Thoughts
You’ve completed 30 days of Python mastery — from syntax to systems-level development. Keep building small projects, automate tasks, and explore frameworks like Flask or FastAPI for your next step.

