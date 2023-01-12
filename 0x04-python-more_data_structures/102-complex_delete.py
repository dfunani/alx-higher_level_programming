#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    a_dict = a_dictionary.copy()
    [a_dictionary.pop(key) for key in a_dict if a_dict[key] == value]
    return a_dictionary
