#!/bin/sh -l

echo "JSON Input $1"
echo "Runner work directory $2"

ls -l $GITHUB_WORKSPACE
ls -l /action

if html_output=$(python /action/src/main.py "$1" "$2"); then
    echo "html-output=$html_output" >> $GITHUB_OUTPUT
else
    echo "Unable return HTML output"
    exit 1
fi

