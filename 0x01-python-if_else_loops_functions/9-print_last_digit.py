#!/usr/bin/python3
def print_last_digit(number):
    if type(number) != int:
        return
    print(number % 10, end="")
    return number % 10
