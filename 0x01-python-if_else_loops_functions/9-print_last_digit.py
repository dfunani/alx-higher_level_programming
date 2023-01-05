#!/usr/bin/python3
def print_last_digit(number):
    if type(number) != int:
        return
    if number >= 0:
        print(number % 10, end="")
        return number % 10
    else:
        print(-number % 10, end="")
        return -number % 10
