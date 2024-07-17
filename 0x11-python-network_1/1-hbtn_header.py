#!/usr/bin/python3
"""send request and display the value of X-Request-Id"""
import urllib.request
import sys

with urllib.request.urlopen(sys.argv[1]) as response:
    html = response.read()
    head = response.headers
value = head.get("X-Request-Id")
print(value)
