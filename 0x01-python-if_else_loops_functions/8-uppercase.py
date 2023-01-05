#!/usr/bin/python3
def islower(c):
    return ord(c) > 96 and ord(c) < 123

def uppercase(str):
    for char in str:
        temp = ""
        if islower(char):
            temp = chr(ord(char) - 32)
        else:
            temp = char
        print("{}".format(temp), end="")
    print()
