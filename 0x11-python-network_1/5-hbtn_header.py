#!/usr/bin/python3
"""Sends a request to the URL and displays variable X-Request-Id"""

if __name__ == '__main__':
    from requests import get
    from sys import argv

     if len(argv) != 2:
         print("Usage: python3 script.py <URL>")
         exit(1)

    res = get(argv[1])
    print(res.headers.get('X-Request-Id'))
