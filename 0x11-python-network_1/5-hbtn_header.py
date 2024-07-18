#!/usr/bin/python3
"""display X-Response-Id of response header"""
import requests
from sys import argv


def main():
    """
    takes in a URL, sends a request to the URL
    and displays the value of the variable
    X-Request-Id in the response header
    """
    res = requests.get(argv[1])
    head = res.headers
    print(head.get('x-request-id'))

if __name__ == "__main__":
    main()
