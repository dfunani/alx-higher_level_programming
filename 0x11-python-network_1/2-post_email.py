#!/usr/bin/python3
""" Module covers a significant component of web servers and clients """
from urllib import request, parse
import sys

if __name__ == "__main__":
    with request.urlopen(sys.argv[1], data=parse.urlencode({"email": sys.argv[2]}).encode('utf-8')) as response:
        print(response.read().decode('utf-8'))
