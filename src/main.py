import sys
from myApp import MyApp;

# from githubkit import GitHub, ActionAuthStrategy
# github = GitHub(ActionAuthStrategy())

containers = []

MyApp.startUp(sys.argv, containers, 'CreateReportAction')