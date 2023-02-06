#!/usr/bin/python3
"""
1-my_list module
"""


class MyList(list):

    def print_sorted(self):
        self.sort()
        for (elem in self):
            print(elem)
