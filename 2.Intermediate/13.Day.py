# Day 13 - Modules and Packages

# --- Importing Built-in Modules ---
import math
print("Square root of 25:", math.sqrt(25))
print("Value of pi:", math.pi)

from math import pow, ceil
print("2 raised to power 3:", pow(2, 3))
print("Ceiling of 4.1:", ceil(4.1))

# --- Using Aliases ---
import math as m
print("Cosine of 0:", m.cos(0))

# --- Importing Specific Functions ---
from math import factorial
print("Factorial of 5:", factorial(5))

# --- Practice Exercises ---

# 1. Random number between 1 and 50
import random
print("Random number between 1 and 50:", random.randint(1, 50))

# 2. Today's date using datetime
from datetime import date
print("Today's Date:", date.today())

# 3. Calculator module example
def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
print("Add:", add(10, 5))
print("Subtract:", subtract(10, 5))

# 4. Utils package example
def reverse_string(s):
    return s[::-1]
print("Reverse:", reverse_string("Modules"))

def even_numbers(lst):
    return [n for n in lst if n % 2 == 0]
print("Even Numbers:", even_numbers([1,2,3,4,5,6]))
