class Action():
    _app = None

    def __init__(self, app):
        self._app = app
        pass

    def exec(self):
        pass

    def injectService(self, serviceName):
        return self._app._di.getService(serviceName, self._app)
    
    def injectConfigByName(self, configName):
        return self._app.getArgumentByName(configName)
