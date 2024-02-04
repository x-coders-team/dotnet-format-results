from models import Argument
from actions import *

class Application():
    _appName = ''
    _args = []
    _di = None
    _action_module = 'actions'
    _service_module = 'services'

    def __init__(self, appName = '', args = [], di = {}):
        self._appName = appName
        self._args = args
        self._di = di
        pass

    @staticmethod
    def startUp(argv, entrypointAction = 'index'):
        pass

    @staticmethod
    def createArgumentsCollection(arg, collection):
        collection.append(arg)
        return collection
    
    @staticmethod
    def createArgument(argName, argValue):
        return Argument(argName, argValue)
    
    def getArgumentByName(self, argName):
        for arg in self._args:
            if arg.getName() == argName:
                return arg.getValue()
            
        return None

    def runAction(self, actionName):
        module = __import__(self._action_module)
        actionClass = getattr(module, actionName)
        return actionClass(self).exec()
