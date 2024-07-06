#!/bin/bash
# This script curl the content length on a page

IP=$1
curl -s "$IP" -I | grep Content-Length | cut -d':' -f 2 >&1
