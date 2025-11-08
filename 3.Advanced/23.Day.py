# Decorators & Context Managers 
# Day 23: Creating a Context Manager with `contextlib`
# Welcome to Day 23 of your Python learning journey! Today, we will explore how to
# create context managers using the `contextlib` module. Context managers are a way to allocate and release resources precisely when you want to.
# They are commonly used for managing file operations, database connections, and more.  
# ## Table of Contents
# 1. [What is a Context Manager?](#what-is-a-context-manager)   
# 2. [Using `contextlib` to Create Context Managers](#using-contextlib-to-create-context-managers)
# 3. [Code Example](#code-example)
# 4. [Practice Exercises](#practice-exercises)
# 
# What is a Context Manager?
# A context manager is a construct that allows you to set up a temporary context for your code
# to run in, and then clean up after itself when the code block is exited.
# The most common way to use a context manager is with the `with` statement.
# This ensures that resources are properly managed, even if an error occurs within the block.
# Using `contextlib` to Create Context Managers
# The `contextlib` module provides utilities for working with context managers and the `with`
# statement. One of the most useful features of `contextlib` is the `contextmanager` decorator,
# which allows you to create a context manager using a generator function.
# Here's an example of how to use the `contextmanager` decorator:
from contextlib import contextmanager

@contextmanager
def my_context_manager():
    # Setup code: executed when entering the context
    print("Entering the context")
    try:
        yield  # This is where the code block inside the 'with' statement will run
    finally:
        # Teardown code: executed when exiting the context
        print("Exiting the context")
# Code Example
# Now, let's see how to use the `my_context_manager` context manager:
# Using the custom context manager
# with my_context_manager():
#     print("Inside the context")
# # Output:
# # Entering the context
# # Inside the context
# # Exiting the context
# Practice Exercises
# 1. Create a context manager that opens a file, writes some data to it, and then closes it.
# 2. Create a context manager that measures the time taken to execute a block of code.
# 3. Create a context manager that temporarily changes the current working directory and then reverts
#   back to the original directory after exiting the context.
# 4. Create a context manager that suppresses specific exceptions within its block.
# Happy coding!
# # # Output:
# Entering the context
# Inside the context
# Exiting the context
# # 1. Create a context manager that opens a file, writes some data to it, and then closes it.
@contextmanager 
def file_writer(file_name, mode='w'):
    try:
        file = open(file_name, mode)
        yield file
    finally:
        file.close()
# Usage
with file_writer('example.txt') as f:
    f.write('Hello, World!')
# 2. Create a context manager that measures the time taken to execute a block of code.
import time

@contextmanager
def timer():
    start_time = time.time()
    yield
    end_time = time.time()
    print(f"Execution time: {end_time - start_time} seconds")
# Usage
with timer():
    total = sum(range(1000000)) 
# 3. Create a context manager that temporarily changes the current working directory and then reverts
# back to the original directory after exiting the context.
import os

@contextmanager
def change_directory(new_path):
    original_path = os.getcwd()
    os.chdir(new_path)
    try:
        yield
    finally:
        os.chdir(original_path)
# Usage
# with change_directory('/path/to/new/directory'):
#     # Code to run in the new directory
# 4. Create a context manager that suppresses specific exceptions within its block.
@contextmanager
def suppress_exceptions(*exceptions):
    try:
        yield
    except exceptions:
        pass
# Usage
with suppress_exceptions(ZeroDivisionError):
    result = 1 / 0  # This will not raise an exception
    print("This line will still execute.")
    print("This line will still execute.")
    print("This line will still execute.")
    print("This line will still execute.")
    print("This line will still execute.")
    print("This line will still execute.")  
    print("This line will still execute.")
print("Exited the context without an exception.")


