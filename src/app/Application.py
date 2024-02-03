from models import Argument
from actions import *

class Application():
    _appName = ''
    _args = []
    _services = dict()
    _action_module = 'actions'
    _service_module = 'services'

    def __init__(self, appName = '', args = [], services = {}):
        self._appName = appName
        self._args = args
        self._services = services
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

    def registryService(self, serviceName):
        if self.isServiceExists(serviceName) == True:
            return
        
        module = __import__(self._service_module)
        serviceClass = getattr(module, serviceName)
        self._services[serviceName] = serviceClass(self._services, self)
        pass

    def updateService(self, serviceName, serviceImpl):
        if self.isServiceExists(serviceName) == False:
            return
        
        module = __import__(self._service_module)
        serviceClass = getattr(module, serviceName)
        self._services[serviceName] = serviceClass(self._services, self)
        pass

    def isServiceExists(self, serviceName):
        if serviceName in self._services:
            return True
        
        return False;

    def getService(self, serviceName):
        if self.isServiceExists(serviceName) == False:
            return None
        
        return self._services[serviceName]

    def runAction(self, actionName):
        module = __import__(self._action_module)
        actionClass = getattr(module, actionName)
        return actionClass(self).exec()
