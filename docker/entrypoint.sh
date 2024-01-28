#!/bin/sh -l

echo "JSON Input $1"
html_output="<html><head><title>Testing</title></head><body><p>Testing workflow</p></body></html>"
echo "html-output=$html_output" >> $GITHUB_OUTPUT
