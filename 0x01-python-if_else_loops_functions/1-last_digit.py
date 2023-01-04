#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
print(f"Last digit of {number} is {number % 10}", end=" ")
if number % 10 == 0:
    print(f"and is 0")
elif number % 10 > 5:
    print(f"and is greater than 5")
else:
    print(f"and is less than 6 and not 0")
