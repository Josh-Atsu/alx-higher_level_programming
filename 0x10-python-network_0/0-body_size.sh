#!/usr/bin/env bash
# sends a request to that URL
# displays the size of the body of the response

curl -s -w '%{size_download}' "$1"
echo ""
