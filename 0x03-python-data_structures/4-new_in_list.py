#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    res = list(my_list)
    if idx >= 0 and idx < len(res):
        res[idx] = element
    return res
