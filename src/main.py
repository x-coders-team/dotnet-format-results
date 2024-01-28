import sys
json_input = sys.argv[1]
html_output = f"<html><head><title>Testing from Python</title></head><body><p>Testing workflow</p><div>{json_input}</div></body></html>"
print(html_output)