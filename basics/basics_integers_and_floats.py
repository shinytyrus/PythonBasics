"""
    This file covers a basic overview of Integers or 'ints' and floats in Python
"""

# Create ints and floats
int_a = 3
float_a = 3.14
print(type(int_a))
print(type(float_a))

# Int/Float basic mathematical operations
int_b = int_a + 3 * (8 // 4)**2 - 10  # 8/4 returns a floating value, that's why we're using flooring
float_b = float_a + 3 * (4.33 / 8)**2 - 0.7
print(int_b)
print(float_b)

# Int Remainder, useful for checking if a number is odd or even
int_c = 16 % 5
print(int_c)

# Int Flooring, i.e. reducing a float to it's closet integer value
int_d = 6 // 5
float_d = 6/5
print(int_d)
print(float_d)

# casting an object to an int
int_e = int(3.24)
float_e = float(3)
print(type(int_e))
print(type(float_e))

# Other useful functions that can be run on an int or a float ->
# https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex
print(dir(int_a))
print(dir(float_a))

