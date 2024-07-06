#!/bin/bash
# This script curl the content length on a page
curl -s "$1" -I | grep Content-Length | cut -d':' -f 2 >&1
