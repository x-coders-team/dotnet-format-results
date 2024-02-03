import sys
from githubkit import GitHub, ActionAuthStrategy

github = GitHub(ActionAuthStrategy())

json_input = sys.argv[1]
runner_workdir = sys.argv[2]

html_output = f"<html><head><title>Testing from Python</title></head><body><p>Testing workflow</p><div>{json_input}</div></body></html>"
print(html_output)