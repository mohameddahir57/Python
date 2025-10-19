# Day 7 -String Manipulation: f-strings, `.upper()`, `.lower()`, `.split()`, `.join()`

# Welcome to Day 7 of your Python learning journey! Today, we'll focus on string manipulation in Python, which is crucial for handling and formatting text data. By the end of this lesson, you'll be proficient in using f-strings, changing case with `.upper()` and `.lower()`, splitting strings with `.split()`, and concatenating strings. You'll also get hands-on practice with these techniques.
## Table of Contents    
#1. [f-Strings](#f-strings)
#2. [Changing Case](#changing-case)
#3. [Splitting Strings](#splitting-strings)
#4. [Concatenation](#concatenation)
#5. [Practice Exercises](#practice-exercises)


## f-Strings
#f-Strings (formatted string literals) allow you to embed expressions inside string literals, using curly braces {}.
name = "Mohamed"
age = 20
greeting = f"Hello, my name is {name} and I am {age} years old."
print(greeting)  # Output: Hello, my name is Mohamed and I am 20 years old.


## Changing Case
#You can change the case of strings using the `.upper()` and `.lower()` methods.
text = "Hello, World!"
print(text.upper())  # Output: HELLO, WORLD!
print(text.lower())  # Output: hello, world!

## Splitting Strings
#The `.split()` method splits a string into a list of substrings based on a specified delimiter (default is whitespace).
sentence = "Python is a great programming language"
words = sentence.split()
print(words)  # Output: ['Python', 'is', 'a', 'great', 'programming', 'language']

## Concatenation
#You can concatenate (join) strings using the `+` operator or the `.join()` method.
first_name = "Mohamed"
last_name = "Dahir"
full_name = first_name + " " + last_name
print(full_name)  # Output: Mohamed Dahir
# Using .join() method
words_list = ["Python", "is", "fun"]
joined_sentence = " ".join(words_list)
print(joined_sentence)  # Output: Python is fun


## Practice Exercises
#1. Create a greeting message using f-strings that includes your name and age.
name = "Your Name"
age = 30
greeting = f"Hello, my name is {name} and I am {age} years old."
print(greeting)

#2. Convert the string "hello world" to uppercase and lowercase.
text = "hello world"
print(text.upper())  # Output: HELLO WORLD
print(text.lower())  # Output: hello world

#3. Split the sentence "Learning Python is fun and exciting" into a list of words.
sentence = "Learning Python is fun and exciting"
words = sentence.split()
print(words)  # Output: ['Learning', 'Python', 'is', 'fun', 'and', 'exciting']

#4. Concatenate the strings "Python", "is", and "awesome" into a single sentence using both `+` operator and `.join()` method.
str1 = "Python"
str2 = "is"
str3 = "awesome"
# Using + operator
sentence1 = str1 + " " + str2 + " " + str3
print(sentence1)  # Output: Python is awesome
# Using .join() method
sentence2 = " ".join([str1, str2, str3])
print(sentence2)  # Output: Python is awesome

#Congratulations on completing Day 7! You've enhanced your skills in string manipulation, which is essential for working with text data in Python. Keep practicing these techniques to become more proficient in handling strings.