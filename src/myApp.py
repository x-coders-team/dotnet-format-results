
from app import Application
from app import DepedencyInjection

class MyApp(Application):
    def __init__(self,appName = '', args=[], services={}):
        super().__init__(appName, args, services)
    
    @staticmethod
    def startUp(argv, containers, entrypointAction = 'index'):

        argumentsCollection = MyApp.prepareArgumentsCollection(argv)

        di = DepedencyInjection(containers);
        di.registryService('ExampleService')
        di.registryService('FileJsonEncoderService')
        di.registryService('MapperDotnetFormatService')
        di.registryService('GitHubChecksService')

        app = MyApp('dotnet-format-results', argumentsCollection, di)
        
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