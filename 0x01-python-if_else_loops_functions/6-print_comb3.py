#!/usr/bin/python3
res = []
for i in range(0, 10):
    for j in range(0, 10):
        if i != j and str(i) + str(j) not in res and str(j) + str(i) not in res:
            res.append(str(i) + str(j))
            if i == 8 and j == 9:
                print("{}".format(str(i) + str(j)))
            else:
                print("{}".format(str(i) + str(j) + ", "), end="")
