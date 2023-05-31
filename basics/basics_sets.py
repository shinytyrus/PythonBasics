"""
    This file covers a basic overview of Sets in Python
"""

# Creating a Set
set_a = {1, 2, 3, 4}
set_b = set([1, 2, 3, 5])
print(type(set_a))
print(type(set_b))
print(set_a)
print(set_b)

# common Set functionalities
max_set = max(set_a)
min_set = min(set_a)
length_set = len(set_a)
difference_set = set_a.difference(set_b)
intersection_set = set_b.intersection(set_a)
print(max_set)
print(min_set)
print(length_set)
print(difference_set)
print(intersection_set)

# Set Manipulation - Sets are mutable
set_a.add(5)
print(set_a)
set_a.remove(4)
print(set_a)
set_a.pop()
print(set_a)
set_a.update(set_b)
print(set_a)
