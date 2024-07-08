#!/bin/bash
# send request and get the status code
curl -sw "%{http_code}" "$1" -o /dev/null
