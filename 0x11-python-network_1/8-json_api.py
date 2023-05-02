#!/usr/bin/python3
""" Module covers a significant component of web servers and clients """
import sys
import requests

if __name__ == "__main__":
    res = requests.post(sys.argv[1], data={"q": sys.argv[2]})
    if not res.json():
        print("No result")
    elif 'id' not in res.json() or 'name' not in res.json():
        print("Not a valid JSON")
    else:
        print(f"[{res.json().get('id')}] {res.json().get('name')}")
