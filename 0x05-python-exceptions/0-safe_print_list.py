#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    sum = 0
    try:
        for i, v in enumerate(my_list):
            if i >= x:
                break
            print(my_list[i], end="")
            sum += 1
    except Exception:
        pass
    print()
    return sum
