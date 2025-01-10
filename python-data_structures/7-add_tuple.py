#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a_tuple = tuple_a + (0,) * (2 - len(tuple_a))
    b_tuple = tuple_b + (0,) * (2 - len(tuple_b))

    max_2_elm_tuple_a = a_tuple[:2]
    max_2_elm_tuple_b = b_tuple[:2]

    res = tuple(map(lambda i, j: i + j, max_2_elm_tuple_a, max_2_elm_tuple_b))

    return res
