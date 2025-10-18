# Day 6 - Data Structures: Lists, tuples, sets, dictionaries. Practice
# Welcome to Day 6 of your Python learning journey! Today, we'll dive into data structures in Python, which are essential for organizing and managing data effectively. By the end of this lesson, you'll be familiar with lists, tuples, sets, and dictionaries, and you'll have hands-on practice with adding, removing, and accessing elements in these data structures.
## Table of Contents
#1. [Lists](#lists)
#2. [Tuples](#tuples)
#3. [Sets](#sets)
#4. [Dictionaries](#dictionaries)
#5. [Practice Exercises](#practice-exercises)

## Lists
#Lists are ordered collections of items that can be changed (mutable). They are defined using square brackets [].   

# Example of a list
fruits = ["apple", "banana", "cherry"]
print(fruits)  # Output: ['apple', 'banana', 'cherry']  
# Adding an item to a list
fruits.append("orange")
print(fruits)  # Output: ['apple', 'banana', 'cherry', 'orange']
# Accessing an item in a list
print(fruits[1])  # Output: banana
# Removing an item from a list
fruits.remove("banana")
print(fruits)  # Output: ['apple', 'cherry', 'orange']


## Tuples
#Tuples are ordered collections of items that cannot be changed (immutable). They are defined using parentheses ().
# Example of a tuple
coordinates = (10, 20)
print(coordinates)  # Output: (10, 20)
# Accessing an item in a tuple
print(coordinates[0])  # Output: 10
# Tuples cannot be modified, so the following line would raise an error:
# coordinates[0] = 15  # This will raise a TypeError


## Sets
#Sets are unordered collections of unique items. They are defined using curly braces {}.
# Example of a set
fruits_set = {"apple", "banana", "cherry"}
print(fruits_set)  # Output: {'apple', 'banana', 'cherry'}
# Adding an item to a set
fruits_set.add("orange")
print(fruits_set)  # Output: {'apple', 'banana', 'cherry', 'orange'}
# Accessing items in a set (Note: sets do not support indexing)
for fruit in fruits_set:
    print(fruit)
# Removing an item from a set
fruits_set.remove("banana")
print(fruits_set)  # Output: {'apple', 'cherry', 'orange'}


## Dictionaries
#Dictionaries are collections of key-value pairs. They are defined using curly braces {} with keys and values separated by colons.
# Example of a dictionary
person = {"name": "Mohamed", "age": 20, "city": "New York"}
print(person)  # Output: {'name': 'Mohamed', 'age': 20, 'city': 'New York'}
# Accessing a value in a dictionary
print(person["name"])  # Output: Mohamed
# Adding a key-value pair to a dictionary
person["job"] = "Engineer"
print(person)  # Output: {'name': 'Mohamed', 'age': 20, 'city': 'New York', 'job': 'Engineer'}
# Removing a key-value pair from a dictionary
del person["age"]
print(person)  # Output: {'name': 'Mohamed', 'city': 'New York', 'job': 'Engineer'}


## Practice Exercises
#1. Create a list of your favorite colors, add a new color, and remove one color.
colors = ["red", "blue", "green"]
colors.append("yellow")
colors.remove("blue")
print(colors)  # Output: ['red', 'green', 'yellow'] 

#2. Create a tuple with your birth date (day, month, year) and access the month.
birth_date = (15, 8, 1990)
print(birth_date[1])  # Output: 8

#3. Create a set of unique numbers, add a new number, and iterate through the set to print each number.
unique_numbers = {1, 2, 3, 4, 5}
unique_numbers.add(6)
for number in unique_numbers:
    print(number)

#4. Create a dictionary with your name, age, and city. Update your age and remove the city.
person = {"name": "Mohamed", "age": 20, "city": "New York"}
person["age"] = 21
del person["city"]
print(person)  # Output: {'name': 'Mohamed', 'age': 21, 'job': 'Engineer'}

#Congratulations on completing Day 6! You've learned about essential data structures in Python that will help you manage and organize data effectively. Keep practicing these concepts to strengthen your understanding.