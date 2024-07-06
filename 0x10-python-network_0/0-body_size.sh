#!/usr/bin/env bash
# sends a request to that URL
curl -s -w '%{size_download}' "$1" && echo ""
