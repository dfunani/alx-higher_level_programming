#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    a_dict = {}
    [a_dict.update({key: v * 2}) for key, v in a_dictionary.items()]
    return a_dict
