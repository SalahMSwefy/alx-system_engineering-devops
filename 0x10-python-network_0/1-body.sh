#!/usr/bin/env bash

if [ $# -eq 0 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

curl -s -L "$1"
