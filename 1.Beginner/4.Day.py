# Day 4: Arithmetic, comparison, logical, and assignment operators — practice with examples.

# Arithmetic Operators
a = 10
b = 5
c = a + b
d = a - b
e = a * b
f = a / b
g = a % b
h = a ** b
i = a // b
print("Arithmetic Operators:")
print("Addition:", c)
print("Subtraction:", d)
print("Multiplication:", e)
print("Division:", f)
print("Modulus:", g)
print("Exponentiation:", h)
print("Floor Division:", i) 
print()


# Comparison Operators
x = 10
y = 5
z = x == y
w = x != y
v = x > y
u = x < y
t = x >= y
s = x <= y
print("Comparison Operators:")
print("Equal to:", z)
print("Not equal to:", w)
print("Greater than:", v)
print("Less than:", u)
print("Greater than or equal to:", t)
print("Less than or equal to:", s)
print()

# Logical Operators
a = True
b = False
c = a and b
d = a or b
e = not a
print("Logical Operators:")
print("AND:", c)
print("OR:", d)
print("NOT:", e)
print()


# Assignment Operators
x = 10
x += 5
x -= 3
x *= 2
x /= 4
x %= 2
x **= 3
x //= 2
print("Assignment Operators:")
print("Add and assign:", x) 
print("Subtract and assign:", x)
print("Multiply and assign:", x)
print("Divide and assign:", x)
print("Modulus and assign:", x)
print("Exponentiate and assign:", x)
print("Floor divide and assign:", x)
print()


# Practice Examples

#1.Example of Arithmetic
length = 5
width = 3
area = length * width
print("Area of rectangle:", area)
print()

#2.Example  Comparison
number = 7
is_even = number % 2 == 0
print("Is the number even?", is_even)
print()

#3.Example  Logical
num = 15
is_in_range = num > 10 and num < 20
print("Is the number between 10 and 20?", is_in_range)
print()

#4.Example  Assignment
count = 0
count += 1
print("Updated count:", count)  
count *= 5
print("Count after multiplication:", count)
count -= 2
print("Count after subtraction:", count)
count //= 3
print("Count after floor division:", count)
count **= 2
print("Count after exponentiation:", count)
count %= 4
print("Count after modulus:", count)
print()
