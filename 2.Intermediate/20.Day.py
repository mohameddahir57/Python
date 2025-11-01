#Day 20-Mini Project – Command Line Tool or Data Script
#Welcome to Day 20 of your Python learning journey! Today, we will explore a mini project that demonstrates the power of command line tools and data scripts in Python.

#Command Line Tools and Data Scripts
#In this mini project, we will create a command line tool and data script that perform specific tasks based on user input. Let's break down the components: 

## Command Line Tool
#A command line tool is a program that allows users to interact with the system in a command-line interface. It provides a way to execute commands and perform actions from the command line.
#In this mini project, we will create a command line tool that allows users to input a name and retrieve a greeting message. Let's look at the code:

import sys

def greet(name):
    print(f"Hello, {name}!")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        name = sys.argv[1]
        greet(name)
    else:
        print("Please provide a name as a command-line argument.")

#In this code, we import the sys module to access command-line arguments. We define a function greet that takes a name as input and prints a greeting message.
#The main block checks if the script is run as the main program and if a name is provided as a command-line argument. If so, it calls the greet function with the name.
#If not, it prints a message indicating that a name is required.
#To use this command line tool, you can run it from the command line with the name as an argument:
#python command_line_tool.py John
#This will print "Hello, Mohamed!"

## Data Script
#A data script is a Python script that generates or processes data and outputs it in a specific format. It can be used for tasks like data cleaning, data analysis, or data transformation.
#In this mini project, we will create a data script that generates a list of square numbers based on a given range. Let's look at the code:

def generate_squares(start, end):
    squares = []
    for num in range(start, end + 1):
        squares.append(num * num)
    return squares

if __name__ == "__main__":
    start = 1
    end = 5
    squares = generate_squares(start, end)
    print(squares)  # Output: [1, 4, 9, 16, 25]

#In this code, we define a function generate_squares that takes a start and end value as input and generates a list of square numbers in the specified range.
#The main block creates a list of square numbers using the generate_squares function and prints the result.
#To use this data script, you can run it from the command line with the start and end values as arguments:
#python data_script.py 1 5
#This will print [1, 4, 9, 16, 25]


