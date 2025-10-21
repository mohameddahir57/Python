#Day 9 - File I/O & Exception Handling: Read/write files, `try/except`
# Welcome to Day 9 of the Python Beginner Course! Today, we'll explore file input/output (I/O) and exception handling in Python. File I/O allows you to read from and write to files, while exception handling helps you manage errors gracefully. By the end of this lesson, you'll be able to work with files and handle exceptions effectively.

## Table of Contents
#1. [File I/O](#file-io)
#2. [Reading Files](#reading-files)
#3. [Writing Files](#writing-files)
#4. [Exception Handling](#exception-handling)
#5. [Practice Exercises](#practice-exercises)


## File I/O
#File I/O in Python is done using built-in functions like `open()`, `read()`, `write()`, and `close()`. You can open files in different modes such as read (`'r'`), write (`'w'`), and append (`'a'`).


## Reading Files
#To read a file, use the `open()` function with the `'r'` mode and then call the `read()` or `readlines()` method.
file = open('example.txt', 'r')
content = file.read()
print(content)  # Output: Contents of the file
file.close()


## Writing Files
#To write to a file, use the `open()` function with the `'w'` mode and then call the `write()` method.
file = open('output.txt', 'w')
file.write("Hello, this is a test file.\n")
file.close()


## Exception Handling
#Exception handling in Python is done using `try`, `except`, `else`, and `finally` blocks. This allows you to catch and handle errors gracefully.
try:
    number = int(input("Enter a number: "))
    result = 10 / number
except ValueError:
    print("Invalid input. Please enter a valid number.")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
else:
    print("Result:", result)
finally:
    print("Execution completed.")


## Practice Exercises
#1. Create a text file named `data.txt` and write a list of your favorite fruits to it, each on a new line.
fruits = ['Apple', 'Banana', 'Cherry', 'Date']
with open('data.txt', 'w') as file:
    for fruit in fruits:
        file.write(fruit + '\n')


#2. Read the contents of `data.txt` and print each fruit in uppercase.
with open('data.txt', 'r') as file:
    for line in file:
        print(line.strip().upper())


#3. Write a program that prompts the user to enter a filename and attempts to read it. Handle the case where the file does not exist using exception handling.
filename = input("Enter the filename to read: ")
try:
    with open(filename, 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("Error: File not found.")

#4. Create a function that takes a filename and a list of strings as parameters, writes the strings to the file, and handles any exceptions that may occur during the process.
def write_to_file(filename, lines):
    try:
        with open(filename, 'w') as file:
            for line in lines:
                file.write(line + '\n')
    except Exception as e:
        print(f"An error occurred: {e}")    
write_to_file('myfile.txt', ['Line 1', 'Line 2', 'Line 3'])

#5. Write a program that divides two numbers provided by the user and handles exceptions for invalid input and division by zero.
def divide_numbers():
    try:
        num1 = float(input("Enter the numerator: "))
        num2 = float(input("Enter the denominator: "))
        result = num1 / num2
    except ValueError:
        print("Invalid input. Please enter numeric values.")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    else:
        print(f"The result is: {result}")
divide_numbers()


#Congratulations on completing Day 9! You've learned how to read from and write to files, as well as how to handle exceptions in Python. These skills are essential for building robust applications that can manage errors gracefully and work with external data. Keep practicing by creating your own file I/O operations and experimenting with different exception handling scenarios!