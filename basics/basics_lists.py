"""
    This file covers a basic overview of Lists in Python
"""

# Creating a List
list_a = [1, 2, 3]
list_b = list((1, 2, 3))
list_c = list("testing")
print(type(list_a))
print(type(list_b))
print(type(list_c))

# common list functionalities
max_list = max(list_b)
min_list = min(list_b)
length_list = len(list_b)
concatenate_lists = list_a + list_b
occurrence_count_list = list_a.count(2)
print(max_list)
print(min_list)
print(length_list)
print(concatenate_lists)
print(occurrence_count_list)

# List Manipulation - List objects are mutable
list_a[0] = 2
print(list_a)
list_a.append(4)
print(list_a)
list_a.insert(1, 10)
print(list_a)
list_a.reverse()
print(list_a)
list_a.pop()
print(list_a)
list_a.remove(2)
print(list_a)
