#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    max_value = my_list[0]

    i = 1
    while i < len(my_list):
        if my_list[i] > max_value:
            max_value = my_list[i]
        i += 1
    return max_value
