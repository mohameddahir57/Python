# Day 13 - Modules and Packages

# --- Importing Built-in Modules ---
import math
print("Square root of 25:", math.sqrt(25))
print("Value of pi:", math.pi)

from math import pow, ceil
print("2 raised to power 3:", pow(2, 3))
print("Ceiling of 4.1:", ceil(4.1))

# --- Importing User-Defined Module ---
# File: mymodule.py
# def greet(name):
#     return f"Hello, {name}!"

# Example of importing it:
# import mymodule
# print(mymodule.greet("Mohamed"))

# --- Using Aliases ---
import math as m
print("Cosine of 0:", m.cos(0))

# --- Importing Specific Functions ---
from math import factorial
print("Factorial of 5:", factorial(5))

# --- Creating a Package Example ---
# Folder: mypackage/
# ├── __init__.py
# ├── operations.py
# └── greetings.py

# operations.py
# def multiply(a, b):
#     return a * b

# greetings.py
# def say_hello():
#     return "Hello from mypackage!"

# Using the package:
# from mypackage import operations, greetings
# print(operations.multiply(2, 3))
# print(greetings.say_hello())

# --- Practice Exercises ---

# 1. Import the random module and print a random number between 1 and 50.
import random
print("Random number between 1 and 50:", random.randint(1, 50))

# 2. Import only the date class from datetime and print today’s date.
from datetime import date
print("Today's Date:", date.today())

# 3. Create a module named calc.py with add() and subtract() functions.
# calc.py
# def add(a, b):
#     return a + b
# def subtract(a, b):
#     return a - b

# In main file:
# import calc
# print(calc.add(10, 5))
# print(calc.subtract(10, 5))

# Example Answer:
def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
print("Add:", add(10, 5))
print("Subtract:", subtract(10, 5))

# 4. Create a package called utils with two modules: strings.py and numbers.py
# strings.py -> reverse_string(s)
# numbers.py -> even_numbers(lst)

# Example Answer:
def reverse_string(s):
    return s[::-1]
print("Reverse:", reverse_string("Modules"))

def even_numbers(lst):
    return [n for n in lst if n % 2 == 0]
print("Even Numbers:", even_numbers([1, 2, 3, 4, 5, 6]))
