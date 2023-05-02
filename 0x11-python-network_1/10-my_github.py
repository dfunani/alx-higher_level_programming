#!/usr/bin/python3
""" Module covers a significant component of web servers and clients """
import sys
import requests

if __name__ == "__main__":
    response = requests.get("https://api.github.com/user",
                            auth=(sys.argv[1], sys.argv[2]))
    print(response.json().get('id'))
