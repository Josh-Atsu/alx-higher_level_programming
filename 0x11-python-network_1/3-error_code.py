#!/usr/bin/python3
"""A script that handles HTTP errors"""
import urllib.request
from sys import argv


def main():
    """
    takes in a URL, sends a request to the URL and
    displays the body of the response (decoded in utf-8).
    manage urllib.error.HTTPError exceptions and
    print: Error code: followed by the HTTP status code
    """
    url = argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            body = response.read().decode('utf-8')
            print(body)
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))

if __name__ == "__main__":
    main()
