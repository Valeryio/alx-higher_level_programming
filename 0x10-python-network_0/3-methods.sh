#!/bin/bash
# This script curl the content length on a page
curl -s -X OPTIONS "$1" | grep Allow | cut -d':' -f 2 >&1
