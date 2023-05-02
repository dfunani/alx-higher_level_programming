#!/usr/bin/python3
""" Module covers a significant component of web servers and clients """
import requests

if __name__ == "__main__":
    response = requests.get("https://alx-intranet.hbtn.io/status").text
    print(f"""Body response:
    - type: {type(response)}
    - content: {response}""")
