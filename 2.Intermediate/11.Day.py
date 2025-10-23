#Day 11 - Advanced Data Structures (Nested lists, dicts, and sets)

#Welcome to Day 11 of your Python learning journey! Today, we will explore advanced data structures in Python, specifically nested lists, nested dictionaries, and nested sets. These structures allow you to store complex data in a more organized way.

#Creating a nested list
nested_list = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

#Accessing elements in a nested list
first_element = nested_list[0][0]  # 1
second_element = nested_list[1][1]  # 5
third_element = nested_list[2][2]  # 9
print("First Element:", first_element)
print("Second Element:", second_element)
print("Third Element:", third_element)

#Creating a nested dictionary
nested_dict = {
    'fruits': {
        'apple': 1,
        'banana': 2
    },
    'vegetables': {
        'carrot': 3,
        'broccoli': 4
    }
}

#Accessing elements in a nested dictionary
apple_count = nested_dict['fruits']['apple']  # 1
banana_count = nested_dict['fruits']['banana']  # 2
carrot_count = nested_dict['vegetables']['carrot']  # 3
broccoli_count = nested_dict['vegetables']['broccoli']  # 4
print("Apple Count:", apple_count)
print("Banana Count:", banana_count)
print("Carrot Count:", carrot_count)
print("Broccoli Count:", broccoli_count)

#Creating a nested set
nested_set = {frozenset({1, 2}), frozenset({3, 4}), frozenset({5, 6})}
#Accessing elements in a nested set
for subset in nested_set:
    print("Subset:", subset)
#Note: Sets are unordered, so the order of subsets may vary

#Practice Exercises
#1. Create a nested list representing a 3x3 matrix and write a function to calculate the sum of each row.

def sum_of_rows(matrix):
    return [sum(row) for row in matrix]

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print("Sum of Rows:", sum_of_rows(matrix))  # Output: [6, 15, 24]

#2. Create a nested dictionary to store information about students and their grades in different subjects. Write a function to calculate the average grade for each student.

def average_grades(students):
    averages = {}
    for student, grades in students.items():
        avg = sum(grades.values()) / len(grades)
        averages[student] = avg
    return averages

students = {
    'Alice': {'Math': 90, 'Science': 85, 'English': 88},
    'Bob': {'Math': 78, 'Science': 82, 'English': 80},
    'Charlie': {'Math': 95, 'Science': 92, 'English': 94}
}
print("Average Grades:", average_grades(students))  # Output: {'Alice': 87.66666666666667, 'Bob': 80.0, 'Charlie': 93.66666666666667}

#3. Create a nested set containing sets of prime numbers and write a function to find the union of all prime number sets.
def union_of_prime_sets(nested_set):
    union_set = set()
    for subset in nested_set:
        union_set.update(subset)
    return union_set
prime_sets = {frozenset({2, 3, 5}), frozenset({7, 11}), frozenset({13, 17, 19})}
print("Union of Prime Sets:", union_of_prime_sets(prime_sets))  # Output: {2, 3, 5, 7, 11, 13, 17, 19}

#4. Create a class `BankAccount` with attributes `account_number` and `balance`. Include methods `deposit` and `withdraw` to modify the balance.
class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return self.balance
        else:
            return "Insufficient funds"
my_account = BankAccount("123456789")
print(my_account.deposit(500))  # Output: 500
print(my_account.withdraw(200))  # Output: 300
print(my_account.withdraw(400))  # Output: Insufficient funds

#Congratulations on completing Day 11! You've learned about nested lists, dictionaries, and sets, as well as how to create a simple class in Python. Keep practicing to strengthen your understanding of these advanced data structures!
