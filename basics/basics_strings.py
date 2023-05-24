"""
    This file covers a basic overview of Strings in Python
"""

# Create Strings using either ' or "
string_a = "Hello World!"
string_b = 'hello World!'

print(type(string_a))
print(type(string_b))

# String Manipulation
string_a2 = string_a + string_b
string_a3 = string_a * 3

print(string_a2)
print(string_a3)

# String Slicing
string_a4 = string_a[1:]
string_a5 = string_a[:1]

print(string_a4)
print(string_a5)

# Check a string prefix or suffix
string_a6 = string_a.endswith('rld!')
string_a7 = string_a.startswith('hell')

print(string_a6)
print(string_a7)

# Check for a substring in a string
if "llo" in string_b:
    print("Yes!")

# Grabbing a character in the string using an index
string_a8 = string_a[2]

print(string_a8)

# Strings are immutable, so they can't be changed (uncomment the below line to test)
# string_a[2] = "t"

# casting an object to a String
int_a = 3
string_a9 = str(int_a)

print(type(string_a9))

# Other useful functions that can be run on a string -
# https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str
print(dir(string_a))

