#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0 and i != 100:
            print("FizzBuzz", end=' ')
        elif i % 3 == 0 and i != 100:
            print("Fizz", end=' ')
        elif i % 5 == 0 and i != 100:
            print("Buzz", end=' ')
        elif i == 100:
            print(i)
        else:
            print(i, end=' ')
