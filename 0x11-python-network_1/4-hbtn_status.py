#!/usr/bin/python3
"""a script that https://alx-intranet.hbtn.io/status"""
import requests

res = requests.get('https://alx-intranet.hbtn.io/status')
r = res.text
print("Body response:\n\t- type: {}\n\t- content: {}".format(type(r), r))
