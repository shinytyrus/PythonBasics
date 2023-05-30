"""
    This file covers a basic overview of Tuples in Python
"""

# Creating a Tuple
tuple_a = ("a", "b")
tuple_b = tuple("abc")
tuple_c = tuple([1, 2, 3])
print(type(tuple_a))
print(type(tuple_b))
print(type(tuple_c))
print(tuple_a)
print(tuple_b)
print(tuple_c)

# common Tuple functionalities
max_list = max(tuple_c)
min_list = min(tuple_c)
length_list = len(tuple_a)
concatenate_lists = tuple_b + tuple_c
occurrence_count_list = tuple_c.count(2)
print(max_list)
print(min_list)
print(length_list)
print(concatenate_lists)
print(occurrence_count_list)

# Hashing - Tuple objects are immutable
hash_a = hash(tuple_b)
print(hash_a)
