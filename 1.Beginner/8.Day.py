# Day 8 - Functions & Modules: Define functions, return values, parameters, lambda, importing modules. Write small reusable functions.
# Welcome to Day 8 of your Python learning journey! Today, we'll dive into functions and modules in Python. Functions are essential for creating reusable code blocks, while modules help organize your code and reuse it across different programs. By the end of this lesson, you'll be able to define functions, work with parameters and return values, use lambda functions, and import modules effectively.
## Table of Contents
#1. [Defining Functions](#defining-functions)
#2. [Return Values](#return-values)
#3. [Parameters](#parameters)
#4. [Lambda Functions](#lambda-functions)
#5. [Importing Modules](#importing-modules)

## Defining Functions
#In Python, you can define a function using the `def` keyword followed by the function name and parentheses.
def greet():
    print("Hello, welcome to Python functions!")    
greet()  # Output: Hello, welcome to Python functions!
    
## Return Values
#You can use the `return` statement to send a value back from a function.
def add(a, b):
    return a + b
result = add(5, 3)
print(result)  # Output: 8

## Parameters
#Functions can take parameters (inputs) to work with different data.
def multiply(x, y):
    return x * y
product = multiply(4, 6)
print(product)  # Output: 24

## Lambda Functions
#Lambda functions are small anonymous functions defined using the `lambda` keyword.
square = lambda x: x ** 2
print(square(5))  # Output: 25

## Importing Modules
#You can import built-in or custom modules using the `import` statement.
import math
print(math.sqrt(16))  # Output: 4.0
#You can also import specific functions from a module.
from math import factorial
print(factorial(5))  # Output: 120

## Practice Exercises
#1. Define a function that takes a name as a parameter and prints a personalized greeting.
def greet_user(name):
    print(f"Hello, {name}! Welcome to Python functions.")

greet_user("Alice")  # Output: Hello, Alice! Welcome to Python functions.

#2. Create a function that calculates the area of a rectangle given its length and width.
def calculate_area(length, width):
    return length * width
area = calculate_area(5, 3)
print(area)  # Output: 15

#3. Write a lambda function that takes a number and returns its cube.
cube = lambda x: x ** 3
print(cube(3))  # Output: 27    

#4. Import the `random` module and use it to generate a random integer between 1 and 10.
import random
print(random.randint(1, 10))  # Output: Random integer between 1 and 10

#5. Define a function that takes a list of numbers and returns a new list with each number squared.
def square_numbers(numbers):
    return [x ** 2 for x in numbers]
squared_list = square_numbers([1, 2, 3, 4, 5])
print(squared_list)  # Output: [1, 4, 9, 16, 25]

#6. Create a function that uses a lambda function to filter out even numbers from a list.
def filter_even_numbers(numbers):
    return list(filter(lambda x: x % 2 != 0, numbers))
odd_numbers = filter_even_numbers([1, 2, 3, 4, 5, 6])
print(odd_numbers)  # Output: [1, 3, 5]

#7. Import the `datetime` module and print the current date and time.
import datetime
now = datetime.datetime.now()
print(now)  # Output: Current date and time
#8. Define a function that takes a string and returns the string reversed.
def reverse_string(s):
    return s[::-1]
reversed_str = reverse_string("Python")
print(reversed_str)  # Output: nohtyP
#9. Create a function that calculates the factorial of a number using recursion.
def recursive_factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * recursive_factorial(n - 1)
fact = recursive_factorial(5)
print(fact)  # Output: 120

#10. Write a function that imports the `os` module and lists all files and directories in the current working directory.
def list_files_and_directories():
    import os
    return os.listdir('.')
files_and_dirs = list_files_and_directories()
print(files_and_dirs)  # Output: List of files and directories in the current working directory

#Congratulations on completing Day 8! You've learned how to define and use functions, work with parameters and return values, utilize lambda functions, and import modules in Python. These skills are fundamental for writing efficient and reusable code. Keep practicing by creating your own functions and exploring different modules to enhance your Python programming abilities!