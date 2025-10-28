#Day 16- Regular Expressions (pattern matching with `re`)
#Welcome to Day 16 of your Python learning journey! Today, we will explore regular expressions (re) in Python, which are used for pattern matching and text manipulation.
## Table of Contents  
#1. [Regular Expressions](#regular-expressions)
#2. [Pattern Matching with `re`](#pattern-matching-with-re)
#3. [Practice Exercises](#practice-exercises)

## Regular Expressions
#Regular expressions (re) are a powerful tool for working with text data in Python. They allow you to match and extract patterns from strings, perform text substitution, and more. Learn how to use regular expressions in Python. 

## Pattern Matching with `re`
#In this section, we will learn how to use regular expressions in Python for pattern matching. We will explore the `re` module and learn how to use it to match specific patterns in strings.
import re

## Regular expression pattern to match a valid email address
email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

# Function to check if a string is a valid email address
def is_valid_email(email):
    return re.match(email_pattern, email)   

# Example usage
email = "Xa9rM@example.com"
if is_valid_email(email):
    print(f"{email} is a valid email address.")
else:
    print(f"{email} is not a valid email address.")

# Output: Xa9rM@example.com is a valid email address.

## [Pattern Matching with `re`](#pattern-matching-with-re)

##  Practice Exercises and Answers 
#1. Write a function that takes a string as input and returns True if it is a valid email address, and False otherwise.

#2. Write a function that takes a string as input and returns True if it is a valid phone number, and False otherwise.

#3. Write a function that takes a string as input and returns True if it is a valid URL, and False otherwise.






