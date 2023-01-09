#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) < 2:
        res = [0, 0]
        if len(tuple_a) == 1:
            res[0] = tuple_a[0]
        tuple_a = tuple(res)
    if len(tuple_b) < 2:
        res = [0, 0]
        if len(tuple_b) == 1:
            res[0] = tuple_b[0]
        tuple_b = tuple(res)

    return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
