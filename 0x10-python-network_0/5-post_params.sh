#!/bin/bash
# send a post request, display the body response message
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
