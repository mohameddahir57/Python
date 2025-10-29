#Day 16-List/Dict Comprehensions and Generators 
#Welcome to Day 16 of your Python learning journey! Today, we will explore list comprehensions, dictionary comprehensions, and generator expressions in Python. These concepts will help you write more concise and efficient code.
## Table of Contents  
#1. [List Comprehensions](#list-comprehensions)
#2. [Dictionary Comprehensions](#dictionary-comprehensions)
#3. [Generator Expressions](#generator-expressions)
#4. [Practice Exercises](#practice-exercises)

#1. Use a list comprehension to create a list of the first 10 even numbers.
even_numbers = [x for x in range(20) if x % 2 == 0]
print(even_numbers)  # Output: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

#2. Create a dictionary using a list comprehension, where the keys are numbers from 1 to 5 and the values are their squares.
squares = {x: x**2 for x in range(1, 6)}
print(squares)  # Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

#3. Use a generator expression to generate the first 10 Fibonacci numbers.
fibonacci = (x for x in [0, 1] + [x + y for x, y in zip(fibonacci, fibonacci[1:])])
print(list(fibonacci))  # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

#4. Create a tuple of the first 5 prime numbers.
primes = tuple(filter(lambda x: all(x % i != 0 for i in range(2, int(x**0.5) + 1)), range(2, 100)))
print(primes)  # Output: (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97)

#5. Use a generator expression to generate the first 10 prime numbers.
primes = (x for x in range(2, 100) if all(x % i != 0 for i in range(2, int(x**0.5) + 1)))
print(list(primes))  # Output: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

#6. Create a list of the first 10 perfect numbers.
perfect_numbers = [x for x in range(1, 1000) if sum(i for i in range(1, x) if x % i == 0) == x]
print(perfect_numbers)  # Output: [6, 28, 496]

# Practice Exercises](#practice-exercises

#1. Write a program that uses a list comprehension to find the prime numbers in a given range.
prime_numbers = [x for x in range(2, 100) if all(x % i != 0 for i in range(2, int(x**0.5) + 1))]
print(prime_numbers)

#2. Create a dictionary using a list comprehension to map numbers to their squares.
squares = {x: x**2 for x in range(1, 6)}
print(squares)

#3. Use a generator expression to generate the first 10 Fibonacci numbers.
fibonacci = (x for x in [0, 1] + [x + y for x, y in zip(fibonacci, fibonacci[1:])])
print(list(fibonacci))

#4. Write a program that uses a generator expression to find the prime numbers in a given range.
prime_numbers = (x for x in range(2, 100) if all(x % i != 0 for i in range(2, int(x**0.5) + 1)))
print(list(prime_numbers))

#5. Create a list of the first 10 perfect numbers.
perfect_numbers = [x for x in range(1, 1000) if sum(i for i in range(1, x) if x % i == 0) == x]
print(perfect_numbers)
