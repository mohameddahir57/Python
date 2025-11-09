# Day 23: Iterators and Generators (custom classes, `__iter__`)
# Welcome to Day 23 of your Python learning journey! Today, we will explore Iterators and Generators in Python, including how to create custom iterator classes using the `__iter__` and `__next__` methods.
# These concepts help you work with sequences of data in a memory-efficient way.
# Table of Contents
# 1. [Iterators and Generators](#iterators-and-generators)
# 2. [Custom Iterator Classes](#custom-iterator-classes)
# 3. [Practice Exercises](#practice-exercises)

# Iterators and Generators
# In Python, an iterator is an object that allows you to iterate over a sequence of elements. You can create an iterator by implementing the `__iter__` and `__next__` methods.
# The `__iter__` method returns the iterator object itself, and the `__next__` method returns the next element in the sequence.
# A generator is a special type of iterator that uses the `yield` keyword instead of `return` to return values.
# You can create a generator by defining a function with the `yield` keyword.
# Iterators and generators are useful when you want to work with large sequences of data in a memory-efficient way.
# Code Example
def count_up_to(max):
    count = 1
    while count <= max:
        yield count
        count += 1
counter = count_up_to(5)
for number in counter:
    print(number)
# Output:
# 1
# 2
# 3
# 4
# 5

# Custom Iterator Classes
# You can create custom iterator classes by defining the `__iter__` and `__next__` methods.
# The `__iter__` method returns the iterator object itself, and the `__next__` method returns the next element in the sequence.
# Code Example
class MyIterator:
    def __init__(self, max):
        self.max = max
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.max:
            number = self.current
            self.current += 1
            return number
        else:
            raise StopIteration
my_iterator = MyIterator(5)
for number in my_iterator:
    print(number)
# Output:
# 1
# 2
# 3
# 4
# 5


# Practice Exercises
# 1. Create a generator function that yields the Fibonacci sequence up to a given number.
def fibonacci_up_to(max):
    a, b = 0, 1
    while a <= max:
        yield a
        a, b = b, a + b
fibonacci = fibonacci_up_to(10)
for number in fibonacci:
    print(number)
# Output:
# 0
# 1
# 1
# 2
# 3
# 5
# 8
# 13
# 21
# 34

# 2. Create a custom iterator class that iterates over the characters of a given string in reverse order.
class ReverseStringIterator:
    def __init__(self, string):
        self.string = string
        self.index = len(string)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index > 0:
            self.index -= 1
            return self.string[self.index]
        else:
            raise StopIteration 
reverse_iterator = ReverseStringIterator("hello")
for char in reverse_iterator:
    print(char)
# Output:
# o
# l
# l
# e
# h
# 3. Write a generator function that yields the squares of numbers from 1 to n.
def squares_up_to(n):
    for i in range(1, n + 1):
        yield i ** 2    
squares = squares_up_to(5)
for square in squares:
    print(square)
# Output:
# 1
# 4
# 9
# 16
# 25