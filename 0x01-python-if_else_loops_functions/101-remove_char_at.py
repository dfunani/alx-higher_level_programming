#!/usr/bin/python3
def remove_char_at(str, n):
    res = ""
    for i, char in enumerate(str):
        if i != n:
            res += char
    return res
