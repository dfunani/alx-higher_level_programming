#!/usr/bin/python3
def no_c(my_string):
    newStr = ""
    [newStr += str for str in my_string if str.lower() != "c"]
    return newStr
