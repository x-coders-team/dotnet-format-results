#!/bin/sh -l

echo "JSON Input $1"

ls -l GITHUB_WORKSPACE

if html_output=$(python ./src/main.py "$1"); then
    echo "html-output=$html_output" >> $GITHUB_OUTPUT
else
    echo "Unable return HTML output"
    exit 1
fi

