#!/usr/bin/python3
"""
a script that sends a POST request
"""
import urllib.request
from sys import argv


def main():
    """
    takes in a URL and an email, sends a POST request
    to the passed URL with the email as a parameter,
    and displays the body of the response (decoded in utf-8)
    """
    data = urllib.parse.urlencode({'email': argv[2]}).encode('utf-8')
    with urllib.request.urlopen(argv[1], data) as response:
        post = response.read().decode('utf-8')
    print(post)

if __name__ == "__main__":
    main()
