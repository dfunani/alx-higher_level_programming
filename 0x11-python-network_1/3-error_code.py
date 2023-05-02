#!/usr/bin/python3
""" Module covers a significant component of web servers and clients """
from urllib import request, error
import sys

if __name__ == "__main__":
    try:
        with request.urlopen(sys.argv[1]) as response:
            print(response.read().decode('utf-8'))
    except error.HTTPError as e:
        print(f"Error code: {e.code}")
