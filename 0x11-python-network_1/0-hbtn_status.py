#!/usr/bin/python3
"""This fetches the url https://alx-intranet.hbtn.io/status"""
import urllib.request


url = "https://alx-intranet.hbtn.io/status"
with urllib.request.urlopen(url) as response:
    http_re = response.read()

print("Body response:\n\t- type: {}\n\t- content: {}\n\t- utf8 content: {}"
      .format(type(http_re), http_re, http_re))
