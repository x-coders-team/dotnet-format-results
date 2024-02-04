import sys
from myApp import MyApp;
from pprint import pprint
from inspect import getmembers
import asyncio

# from githubkit import GitHub, ActionAuthStrategy
# github = GitHub(ActionAuthStrategy())

containers = []
asyncio.run(MyApp.startUp(sys.argv, containers, 'CreateReportAction'))