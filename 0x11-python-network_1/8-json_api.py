#!/usr/bin/python3
"""A POST request"""

import requests
from sys import argv


def main():
    """
    takes in a letter and sends a POST request to
    http://0.0.0.0:5000/search_user with the letter as a parameter.
    """
    if len(argv) < 2:
        q = ""
    else:
        q = argv[1]
    value = {'q': q}
    response = requests.post("http://0.0.0.0:5000/search_user", data=value)
    try:
        r = response.json()
        if bool(r) is False:
            print("No results")
        else:
            print("[{}] {}".format(r['id'], r['name']))
    except:
        print("Not a valid JSON")


if __name__ == "__main__":
    main()
