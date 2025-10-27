# Day 15- Error Handling & Debugging (custom exceptions, logging)
# Welcome to Day 15 of the Python Intermediate Course! Today, we'll explore error handling and debugging in Python, including custom exceptions and logging for better error reporting. By the end of this lesson, you'll have the skills to handle common errors and debug your code effectively.
## Table of Contents    
#1. [Custom Exceptions](#custom-exceptions)
#2. [Logging](#logging)
#3. [Practice Exercises](#practice-exercises)

## Custom Exceptions
#In Python, you can create custom exceptions by defining a new class that inherits from the built-in `Exception` class.
class CustomException(Exception):
    pass

#You can then raise these exceptions to signal specific error conditions in your code.
try:
    raise CustomException("This is a custom exception")
except CustomException as e:
    print(e)

## Logging
#Python provides the `logging` module to log messages and errors in your code. Here's an example of using the logging module to log an error message:
import logging

logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

try:
    result = 10 / 0
except ZeroDivisionError as e:
    logging.error(e)

## Practice Exercises
#1. Create a custom exception called `InvalidInputError` that inherits from `Exception`.    
class InvalidInputError(Exception):
    pass

#2. Write a function that takes two numbers as input and raises `InvalidInputError` if either number is negative.
def validate_input(num1, num2):
    if num1 < 0 or num2 < 0:
        raise InvalidInputError("Both numbers must be non-negative.")

#3. Use the `try`-`except` block to handle the `InvalidInputError` exception and print an error message.
try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    validate_input(num1, num2)
    result = num1 / num2
    print("Result:", result)
except InvalidInputError as e:
    print("Error:", e)

#4. Log the error message using the `logging` module.
import logging

logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    validate_input(num1, num2)
    result = num1 / num2
    print("Result:", result)
except InvalidInputError as e:
    logging.error(e)










