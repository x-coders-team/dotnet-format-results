
from app import Application

class MyApp(Application):
    def __init__(self,appName = '', args=[], services={}):
        super().__init__(appName, args, services)
    
    @staticmethod
    def startUp(argv, entrypointAction = 'index'):
        argumentsCollection = MyApp.prepareArgumentsCollection(argv)        
        app = MyApp('dotnet-format-results', argumentsCollection)

        app.registryService('ExampleService')

        app.runAction(entrypointAction)
        pass 
    
    @staticmethod
    def prepareArgumentsCollection(argv):
        argumentsCollection = []
        argumentsCollection = MyApp.createArgumentsCollection(
            arg = MyApp.createArgument('json_input', argv[1]),
            collection = argumentsCollection
        )
        argumentsCollection = MyApp.createArgumentsCollection(
            arg = MyApp.createArgument('runner_workdir', argv[2]),
            collection = argumentsCollection
        )

        return argumentsCollection