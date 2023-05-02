#!/usr/bin/python3
""" Module covers a significant component of web servers and clients """
from urllib import request
import sys

if __name__ == "__main__":
    with request.urlopen(sys.argv[1]) as response:
        print(response.getheader("X-Request-Id"))
