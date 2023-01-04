#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
var = number % 10
if number < 0:
    var = (number * -1 % 10) * -1
print(f"Last digit of {number} is {var}", end=" ")
if var == 0:
    print(f"and is 0")
elif var > 5:
    print(f"and is greater than 5")
else:
    print(f"and is less than 6 and not 0")
