#!/usr/bin/python3
for i, v in enumerate(range(122, 96, -1)):
    temp = ""
    if i % 2 == 0:
        temp = chr(v)
    else:
        temp = chr(v - 32)
    print(temp, end="")
