#!/bin/bash
# This script curl a page
# curl -s --data-urlencode "email=test@gmail.com&subject=I will always be here for PLD" "$1"
curl -s -d "email=test@gmail.com&subject=I%20will%20always%20be%20here%20for%20PLD" "$1"
