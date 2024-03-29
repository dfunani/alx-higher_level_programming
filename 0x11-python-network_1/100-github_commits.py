#!/usr/bin/python3
""" Module covers a significant component of web servers and clients """
import requests
from sys import argv as a

if __name__ == "__main__":
    api = f"https://api.github.com/repos/{a[2]}/{a[1]}/commits?per_page=10"
    commits = requests.get(api).json()
    for c in commits:
        print(f"{c.get('sha')}: {c.get('commit').get('author').get('name')}")
