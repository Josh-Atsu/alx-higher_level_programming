#!/usr/bin/python3
"""GitHub API"""
import requests
from sys import argv


def main():
    """
    Python script that takes your GitHub credentials
    (username and password)
    and uses the GitHub API to display your id
    """
    username = argv[1]
    passwd = argv[2]
    response = requests.get("https://api.github.com/user",
                            auth=(username, passwd))
    if (response.status_code == 200):
        user_data = response.json()
        user_id = user_data['id']
        print(user_id)
    else:
        print("None")


if __name__ == "__main__":
    main()
