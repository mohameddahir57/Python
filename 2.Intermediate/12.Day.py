# Day 12 - Advanced Functions (*args, **kwargs, recursion, scope)

# Welcome to Day 12 of your Python learning journey! Today, we will explore advanced functions in Python, specifically *args, **kwargs, recursion, and scope. These concepts will help you write more flexible and powerful functions.

# Args : Using *args to pass a variable number of arguments to a function
def sum_all(*args):
    return sum(args)
print("Sum of all numbers:", sum_all(1, 2, 3, 4, 5))  # Output: 15

# Kwargs : Using **kwargs to pass a variable number of keyword arguments to a function
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
print_info(name="Alice", age=30, city="New York")

# Recursion : A function that calls itself
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
print("Factorial of 5:", factorial(5))

# Scope : The region of the program where a variable is defined
x = 10
def outer_function():
    y = 5
    def inner_function():
        z = 2
        print(x, y, z)
    inner_function()
outer_function()

# Practice Exercises
# 1. Write a function that takes any number of arguments and returns their average.
def average(*args):
    if not args:
        return 0
    return sum(args) / len(args)    
print("Average:", average(10, 20, 30, 40))  # Output: 25.0

# 2. Write a function that takes any number of keyword arguments and returns a formatted string of the information.
def format_info(**kwargs):
    return ', '.join(f"{key}: {value}" for key, value in kwargs.items())
print(format_info(name="Mohamed", age=22, country="Somalia"))

# 3. Write a recursive function to compute the nth Fibonacci number.
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
print("Fibonacci of 6:", fibonacci(6))  # Output: 8

# 4. Demonstrate variable scope by creating a function that modifies a global variable.
counter = 0
def increment_counter():
    global counter
    counter += 1
increment_counter()
increment_counter()
print("Counter:", counter)  # Output: 2

# Congratulations on completing Day 12! You've learned about advanced functions in Python, including *args, **kwargs, recursion, and scope. Keep practicing to master these concepts!

