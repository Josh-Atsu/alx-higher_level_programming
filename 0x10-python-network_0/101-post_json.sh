#!/bin/bash
# send a POST request of a JSON file, and display all body response message
curl -s -X POST -H "Content-Type: application/json" -d @"$2" "$1" 
