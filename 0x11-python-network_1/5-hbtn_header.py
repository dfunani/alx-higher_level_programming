#!/usr/bin/python3
""" Module covers a significant component of web servers and clients """
import requests, sys

if __name__ == "__main__":
    response = requests.get(sys.argv[1]).headers
    print(response.get('X-Request-Id'))
