class ServiceAbstract():
    _di = None
    _app = None

    def __init__(self, di = None, app = None):
        self._di = di
        self._app = app
        pass

    def injectService(self, serviceName):
        return self._di.getService(serviceName, self._app)
    
    def injectConfigByName(self, configName):
        return self._app.getArgumentByName(configName)

