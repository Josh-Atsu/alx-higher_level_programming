#!/usr/bin/python3
"""send request and display the value of X-Request-Id"""
import urllib.request
import sys


def main():
    """
    takes in a URL, sends a request to the URL
    and displays the value of the X-Request-Id
    variable found in the header of the response.
    """
    with urllib.request.urlopen(sys.argv[1]) as response:
        html = response.read()
        head = response.headers
    value = head.get("X-Request-Id")
    print(value)

if __name__ == "__main__":
    main()
