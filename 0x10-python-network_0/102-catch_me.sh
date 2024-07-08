#!/bin/bash
# server respond with the message 'you got me'
curl -sL -X PUT -d "user_id=98" -H "Origin: HolbertonSchool" "$1"
