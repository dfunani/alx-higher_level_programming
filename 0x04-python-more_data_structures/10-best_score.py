#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    for i in a_dictionary:
        if a_dictionary[i] == max(a_dictionary.values()):
            return i
