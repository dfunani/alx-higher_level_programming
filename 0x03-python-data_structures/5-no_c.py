#!/usr/bin/python3
def no_c(my_string):
    newStr = ""
    for str in my_string:
        if str.lower() != "c":
            newStr += str
    return newStr
