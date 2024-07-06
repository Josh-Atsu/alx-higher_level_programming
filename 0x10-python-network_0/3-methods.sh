#!/bin/bash
# send request and display all HTTP methods the server will accept
curl -sI "$1"
