#!/usr/bin/python3
"""display X-Response-Id of response header"""
import requests
from sys import argv

res = requests.get(argv[1])
head = res.headers
print(head.get('x-request-id'))
