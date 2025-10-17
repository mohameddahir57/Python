
# Day 5 - Control Flow: if/elif/else, for loops, while loops, list comprehensions

#Welcome to Day 5 of your Python learning journey! Today, we'll explore control flow in Python, which allows you to dictate the flow of your program based on conditions and loops. By the end of this lesson, you'll be comfortable using `if`, `elif`, and `else` statements, as well as `for` and `while` loops, and you'll get introduced to list comprehensions.
## Table of Contents
#1. [Conditional Statements](#conditional-statements)
#2. [Loops](#loops)
#3. [List Comprehensions](#list-comprehensions)  
#4. [Practice Exercises](#practice-exercises)
## Conditional Statements
#Conditional statements allow you to execute certain blocks of code based on whether a condition is true or false

# Example of if, elif, and else
age = 18
if age < 18:
    print("You are a minor.")
elif age == 18:
    print("You are exactly 18.")
else:
    print("You are an adult.")

## Loops
#Loops allow you to repeat a block of code multiple times.
# Example of a for loop
for i in range(5):
    print(f"Iteration {i}")

# Example of a while loop
count = 0
while count < 5:
    print(f"Count is {count}")
    count += 1  

## List Comprehensions
#List comprehensions provide a concise way to create lists.
# Example of a list comprehension
squares = [x**2 for x in range(10)] 
print(squares)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]


## Practice Exercises
#1. Write a program that checks if a number is even or odd using an if/else statement.
number = 4
if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

#2. Create a for loop that prints the numbers from 1 to 10.
for i in range(1, 11):
    print(i)
        
#3. Write a while loop that counts down from 5 to 1.
count = 5
while count > 0:
    print(count)
    count -= 1

#4. Use a list comprehension to create a list of the first 10 even numbers.
even_numbers = [x for x in range(20) if x % 2 == 0]
print(even_numbers)  # Output: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

#Great job on completing Day 5! You've learned how to control the flow of your programs using conditional statements and loops, as well as how to create lists efficiently with list comprehensions. Keep practicing these concepts to solidify your understanding. See you on Day 6!