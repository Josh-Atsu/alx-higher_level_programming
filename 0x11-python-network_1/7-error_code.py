#!/usr/bin/python3
""" Error code detection """
import requests
from sys import argv


def main():
    """
    takes in a URL, sends a request to the URL
    and displays the body of the response

    If the HTTP status code is greater than or equal to 400,
    print: Error code: followed by the value of the HTTP status code
    """
    url = argv[1]
    response = requests.get(url)
    status = response.status_code
    if status >= 400:
        print("Error code: {}".format(status))
    else:
        res = response.text
        print(res)


if __name__ == "__main__":
    main()
