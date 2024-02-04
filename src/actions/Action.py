class Action():
    _app = None

    def __init__(self, app):
        self._app = app
        pass

    def exec(self):
        pass

    def injectService(self, serviceName):
        return self._app._di.getService(serviceName)
