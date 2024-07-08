#!/bin/bash
# send a post request, display the body response message
curl -sX "POST" -d "email=test@gmail.com7&subject=I will always be here for PLD" "$1"
