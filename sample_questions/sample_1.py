"""
    Sample Questions
"""
import time


def some_func(num: int) -> int:
    """
    Some function
    :param num:
    :return:
    """
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return some_func(num-1) + some_func(num-2)


cache = {0: 0, 1: 1}


def some_improved_func(num: int) -> int:
    """
    Some function
    :param num:
    :return:
    """
    if num in cache:
        return cache[num]

    cache[num] = some_improved_func(num-1) + some_improved_func(num-2)
    return cache[num]


give_me_a_number = 5

start_time = time.time()
result = some_func(give_me_a_number)
end_time = time.time()

total_time = end_time - start_time

print(result)
print(total_time)


start_time = time.time()
result = some_improved_func(give_me_a_number)
end_time = time.time()

total_time = end_time - start_time

print(result)
print(total_time)
print(cache)