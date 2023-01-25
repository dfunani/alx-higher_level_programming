#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    sum = 0
    j = 0
    try:
        for i, v in enumerate(my_list):
            if type(v) != int:
                continue
            if i > x:
                break
            print("{:d}".format(my_list[i]), end='')
            sum += 1
            j = i
        if x > j:
            raise IndexError
    except IndexError as e:
        print(e)
    print()
    return sum
