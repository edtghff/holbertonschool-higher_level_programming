#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    i = 0
    copy_list = my_list[:]

    if idx >= 0 and idx < len(copy_list):
        copy_list[idx] = element
        return copy_list
    else:
        return copy_list
