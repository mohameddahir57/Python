#Day 28 : Unit Testing (`unittest` and `pytest`) 
#Welcome to Day 28 of your Python learning journey! Today, we will explore unit testing in Python using the built-in `unittest` module and the popular third-party library `pytest`. Unit testing is essential for ensuring that your code works as expected and helps catch bugs early in the development process.
#Table of Contents
#1. [Using `unittest` for Unit Testing](#using-unittest-for-unit-testing)
#2. [Using `pytest` for Unit Testing](#using-pytest-for-unit-testing)
#3. [Practice Exercises](#practice-exercises)

#Using `unittest` for Unit Testing
#The `unittest` module is a built-in Python library for writing and running tests.
import unittest 
# Example function to be tested
def add(a, b):
    return a + b    
# Unit test for the add function
class TestAddFunction(unittest.TestCase):
    def test_add_positive_numbers(self):
        self.assertEqual(add(2, 3), 5)
    def test_add_negative_numbers(self):
        self.assertEqual(add(-2, -3), -5)
    def test_add_zero(self):
        self.assertEqual(add(0, 5), 5)  
# Run the tests
if __name__ == '__main__':
    unittest.main()

#Using `pytest` for Unit Testing
#`pytest` is a third-party testing framework that makes it easy to write simple and scalable
# tests. You need to install `pytest` if you haven't already:
# pip install pytest
# Example function to be tested
def add(a, b):
    return a + b    
# Unit test for the add function
def test_add_positive_numbers():
    assert add(2, 3) == 5
    assert add(-2, -3) == -5
    assert add(0, 5) == 5    
# Run the tests
if __name__ == '__main__':
    pytest.main()   

#Practice Exercises
#1. Write unit tests for a function that calculates the factorial of a number using both `unittest` and `pytest`.
import unittest
import pytest
# Function to calculate the factorial of a number
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
# Unit test for the factorial function
class TestFactorialFunction(unittest.TestCase):
    def test_factorial_of_zero(self):
        self.assertEqual(factorial(0), 1)
    def test_factorial_of_positive_number(self):
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(3), 6)
    def test_factorial_of_negative_number(self):
        with self.assertRaises(RecursionError):
            factorial(-5)
        with self.assertRaises(RecursionError):
            factorial(-1)
# Run the tests
if __name__ == '__main__':
    unittest.main()
    pytest.main()

#2. Write unit tests for a function that checks if a string is a palindrome using both `unittest` and `pytest`.
import unittest
import pytest
# Function to check if a string is a palindrome
def is_palindrome(string):
    return string == string[::-1]
# Unit test for the is_palindrome function
class TestIsPalindromeFunction(unittest.TestCase):
    def test_palindrome_string(self):
        self.assertTrue(is_palindrome("racecar"))
        self.assertTrue(is_palindrome("madam"))
    def test_non_palindrome_string(self):
        self.assertFalse(is_palindrome("hello"))
        self.assertFalse(is_palindrome("python"))
# Run the tests
if __name__ == '__main__':
    unittest.main()
    pytest.main()   

#3. Write unit tests for a function that sorts a list of numbers using both `unittest` and `pytest`.
import unittest
import pytest
# Function to sort a list of numbers
def sort_numbers(numbers):
    return sorted(numbers)
# Unit test for the sort_numbers function
class TestSortNumbersFunction(unittest.TestCase):
    def test_sort_unsorted_list(self):
        self.assertEqual(sort_numbers([3, 1, 2]), [1, 2, 3])
    def test_sort_already_sorted_list(self):
        self.assertEqual(sort_numbers([1, 2, 3]), [1, 2, 3])
    def test_sort_empty_list(self):
        self.assertEqual(sort_numbers([]), [])
# Run the tests
if __name__ == '__main__':
    unittest.main()
    pytest.main()
# Note: To run the `pytest` tests, save the test functions in a separate file (e.g., `test_script.py`) and run `pytest test_script.py` from the command line.   
# Remember to run the `unittest` tests by executing the script directly.
