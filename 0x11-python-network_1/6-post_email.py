#!/usr/bin/python3
""" Module covers a significant component of web servers and clients """
import sys
import requests

if __name__ == "__main__":
    response = requests.post(sys.argv[1], data={"email": sys.argv[2]})
    print(response.text)
