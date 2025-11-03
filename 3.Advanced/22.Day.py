#Day 21-Functional Programming (map, filter, reduce, lambda)
#Welcome to Day 22 of your Python learning journey! Today, we will explore Functional Programming in Python, including map, filter, reduce, and lambda functions. These concepts help you write more concise and efficient code by applying functions to collections of data.
## Table of Contents
#1. [Map](#map)
#2. [Filter](#filter)
#3. [Reduce](#reduce)
#4. [Lambda Functions](#lambda-functions)
#5. [Practice Exercises](#practice-exercises)

# Map
# The `map()` function applies a given function to all items in an iterable (like a list)
# and returns a map object (which is an iterator).
# You can convert the map object to a list or other iterable types.
# The `map()` function is often used to apply a function to each item in a list, tuple, or other iterable.

# Code Example
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers)

# Output: [1, 4, 9, 16, 25]

## Filter
# The `filter()` function constructs an iterator from elements of an iterable
# for which a function returns True.
# You can convert the filter object to a list or other iterable types.
# The `filter()` function is often used to filter out elements from an iterable based on a condition.

# Code Example
numbers = [1, 2, 3, 4, 5]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)

# Output: [2, 4]

## Reduce
# The `reduce()` function from the `functools` module applies a binary function
# to an iterable to reduce it to a single value.
# You can convert the reduce object to a list or other iterable types.
# The `reduce()` function is often used to reduce a collection of values to a single value.

# Code Example
from functools import reduce

numbers = [1, 2, 3, 4, 5]
sum_of_numbers = reduce(lambda x, y: x + y, numbers)
print(sum_of_numbers)

# Output: 15

## Lambda Functions
# Lambda functions are small anonymous functions defined using the `lambda` keyword.
# They are useful when you need a simple function for a short period, such as in sorting or filtering.

# Code Example
square = lambda x: x ** 2
print(square(5))  # Output: 25


## Practice Exercises
# 1. Use the `map()` function to convert a list of temperatures in Celsius to Fahrenheit.
celsius_temps = [0, 20, 37, 100]
fahrenheit_temps = list(map(lambda c: (c * 9/5) + 32, celsius_temps))
print(fahrenheit_temps)  # Output: [32.0, 68.0, 98.6, 212.0]


# 2. Use the `filter()` function to extract all the odd numbers from a list.
numbers = [1, 2, 3, 4, 5]
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print(odd_numbers)  # Output: [1, 3, 5]

# 3. Use the `reduce()` function to find the product of all numbers in a list.
from functools import reduce
numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)
print(product)  # Output: 120

# 4. Write a lambda function that takes two arguments and returns their maximum value.

max_value = lambda a, b: a if a > b else b
print(max_value(5, 10))  # Output: 10   