"""
    This file covers a basic overview of Integers or 'ints' and floats in Python
"""

# Create ints and floats
int_a = 3
float_a = 3.14

print(type(int_a))
print(type(float_a))

# Int/Float basic mathematical operations
int_b = int_a + 3 * (4 / 8)**2 - 10
float_b = float_a + 3 * (4.33 / 8)**2 - 0.7

print(int_b)
print(float_b)

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

