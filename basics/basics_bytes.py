"""
    This file covers a basic overview of Bytes in Python
"""

# Creating Bytes
bytes_a = b'test'
string_a = "helloWorld!"
bytes_b = bytes(string_a, encoding="utf-8")
print(type(bytes_a))
print(bytes_a)
print(type(bytes_b))
print(bytes_b)

# common Bytes functionalities
bytes_c = bytes_b.removeprefix(b"hello")
print(bytes_c)
bytes_d = bytes_a.decode(encoding="utf-8")
print(type(bytes_d))
print(bytes_d)

# Bytes objects are immutable
bytes_b.removeprefix(b"hello")
print(bytes_b)  # As you can see, the original object isn't modified, meaning it's immutable
