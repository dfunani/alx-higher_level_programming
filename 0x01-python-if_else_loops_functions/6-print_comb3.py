#!/usr/bin/python3
for i in range(0, 9):
    for j in range(i + 1, 10):
        if i == 8 and j == 9:
            print("{}".format(str(i) + str(j)))
        else:
            print("{}".format(str(i) + str(j)), end=", ")
