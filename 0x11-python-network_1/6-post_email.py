#!/bin/python3
"""POST to email"""
import requests
from sys import argv


def main():
    """
    takes in a URL and an email address, 
    sends a POST request to the passed URL with the email as a parameter,
    and finally displays the body of the response.

    The email must be sent in the variable email
    """
    payload = {'email': argv[2] }
    res = requests.post(argv[1], data=payload)
    print(res.text)


if __name__ == "__main__":
    main()
