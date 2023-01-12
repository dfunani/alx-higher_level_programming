#!/usr/bin/python3
def weight_average(my_list=[]):
    a = map(lambda x: x[0] * x[1], my_list)
    b = map(lambda y: y[1], my_list)
    if not my_list:
        return 0
    return sum(list(a)) / sum(list(b))
