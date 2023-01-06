#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    methods = dir(hidden_4)
    for method in methods:
        if method[0:2] != "__":
            print("{}".format(method))
