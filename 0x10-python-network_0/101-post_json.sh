#!/bin/bash
# send a POST request of a JSON file, and display all body response message
curl -sX POST -d "$2" "$1"
