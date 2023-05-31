"""
    This file covers a basic overview of Bytearrays in Python
"""

# Creating Bytearray
bytearray_a = bytearray('test', encoding="utf-8")
string_a = "helloWorld!"
bytearray_b = bytearray(string_a, encoding="utf-8")
print(type(bytearray_a))
print(bytearray_a)
print(type(bytearray_b))
print(bytearray_b)

# common Bytearray functionalities
bytearray_c = bytearray_b.removeprefix(b"hello")
print(bytearray_c)
bytearray_d = bytearray_a.decode(encoding="utf-8")
print(type(bytearray_d))
print(bytearray_d)

# Bytearray objects are mutable
bytearray_b[5:] = bytearray("testing", encoding="utf-8")
print(bytearray_b)