#!/usr/bin/python3
"""Module covers a significant component of web servers and clients """
from urllib import request

if __name__ == "__main__":
    with request.urlopen("https://alx-intranet.hbtn.io/status") as response:
        body = response.read()
        print(f"Body response:")
        print(f"\t- type: type({body}")
        print(f"\t- content: {body}")
        print(f"\t- utf8 content: {body.decode('utf-8')}")
