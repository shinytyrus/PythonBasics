"""
    This file covers a basic overview of how to do comparisons using different types
"""
import json

# Strings
string_a = "Hello"
string_b = "hello"
string_c = string_a
string_d = "ell"

if string_a != string_b:
    print("Strings aren't the same")
else:
    print("Strings are the same")

if string_c is string_a:
    print("Both are identical (i.e. their memory address is the same)")
else:
    print("They aren't identical")

if string_d in string_b:
    print("string_b contains string_d")
else:
    print("string_b doesn't contain string_d")

# Integers/Float
x = 3
y = 4
z = 3.5
a = 4

if x > y:
    print("X is greater than Y")
else:
    print("X is less than Y")

if z < y:
    print("Z is less than Y")
else:
    print("Z is greater than Y")

if y == a:
    print("Y and A are the same")
else:
    print("Y and A aren't the same")

if a <= y:
    print("A is less than or equal to Y")
else:
    print("A is greater than Y")

if x < y <= z:
    print("X is less than Y and Y is less than or equal to Z")
else:
    print("X is greater than Y or Y is greater than Z")
