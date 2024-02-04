import sys
from myApp import MyApp;
from pprint import pprint
from inspect import getmembers

# from githubkit import GitHub, ActionAuthStrategy
# github = GitHub(ActionAuthStrategy())

containers = []
MyApp.startUp(sys.argv, containers, 'CreateReportAction')