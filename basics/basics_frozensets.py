"""
    This file covers a basic overview of Frozensets in Python
"""

# Creating a Frozenset
frozenset_a = frozenset({1, 2, 3, 4})
frozenset_b = frozenset([1, 2, 3, 5])
print(type(frozenset_a))
print(type(frozenset_b))
print(frozenset_a)
print(frozenset_b)

# common Frozenset functionalities
max_set = max(frozenset_a)
min_set = min(frozenset_a)
length_set = len(frozenset_a)
difference_set = frozenset_a.difference(frozenset_b)
print(max_set)
print(min_set)
print(length_set)
print(difference_set)

# Hashing - Frozenset objects are immutable
hash_a = hash(frozenset_a)
print(hash_a)