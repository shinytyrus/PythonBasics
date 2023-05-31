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
max_fset = max(frozenset_a)
min_fset = min(frozenset_a)
length_fset = len(frozenset_a)
difference_fset = frozenset_a.difference(frozenset_b)
intersection_fset = frozenset_b.intersection(frozenset_a)
print(max_fset)
print(min_fset)
print(length_fset)
print(difference_fset)
print(intersection_fset)

# Hashing - Frozenset objects are immutable
hash_a = hash(frozenset_a)
print(hash_a)