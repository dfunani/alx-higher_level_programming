#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    a_dict = a_dictionary.copy()
    [a_dictionary.pop(key) for i in a_dict if i == key]
    return a_dictionary
