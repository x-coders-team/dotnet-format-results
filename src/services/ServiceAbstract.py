class ServiceAbstract():
    _di = None

    def __init__(self, di = None):
        self._di = di
        pass

    def injectService(self, serviceName):
        return self._di.getService(serviceName)
