#!/usr/bin/python3
"""100-my_int
int comp
"""


class MyInt(int):
    """Num handler"""
    def __eq__(self, value):
        """ comp ints"""
        return super().__ne__(value)

    def __ne__(self, value):
        return super().__eq__(value)
