#!/usr/bin/python3
"""1-my_list module
creates class
"""


class MyList(list):
    """ class my_list"""
    def print_sorted(self):
        """ method to print"""
        print(sorted(self))
