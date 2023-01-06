#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    res = 0
    for i in range(1, len(argv)):
        res += int(argv[i])
    print("{}".format(res))
