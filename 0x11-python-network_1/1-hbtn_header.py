#!/usr/bin/python3
""" taking URL as argument and sending as request """


if __name__ == "__main__":
    import urllib.request
    import sys

    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        request_id = response.headers["X-Request-Id"]
        print(request_id)
