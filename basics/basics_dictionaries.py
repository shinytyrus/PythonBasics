"""
    This file covers a basic overview of Dictionaries in Python
"""

# Creating a Dictionary
dict_a = {"test": 1}
dict_b = dict(test=1, test_2=2)
dict_c = dict([("test", 1), ("test2", 2)])
print(type(dict_a))
print(type(dict_b))
print(type(dict_c))

# common list functionalities
length_dict = len(dict_b)
get_key_dict = dict_b.get("test")
keys_dict = dict_b.keys()
view_dict = dict_b.items()
values_dict = dict_b.values()
list_dict = list(dict_b)
key_value_1_dict = dict_b["test"]
print(length_dict)
print(get_key_dict)
print(keys_dict)
print(view_dict)
print(values_dict)
print(list_dict)
print(key_value_1_dict)

# List Manipulation - List objects are mutable
dict_b["test"] = "helloWorld!"
print(dict_b)
del dict_b["test"]
print(dict_b)
dict_b.update({"abc": 2})
print(dict_b)
dict_b.pop("abc")
print(dict_b)
