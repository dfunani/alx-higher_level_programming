#!/usr/bin/python3
""" Module covers a significant component of web servers and clients """
import sys
import requests

if __name__ == "__main__":
    response = requests.get(sys.argv[1])
    if response.status_code >= 400:
        print(f"Error code: {response.status_code}")
    else:
        print(response.text)
