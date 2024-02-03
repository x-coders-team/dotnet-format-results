class ServiceAbstract():
    _di = {}
    _app = None

    def __init__(self, di = {}, app = None):
        self._di = di
        self._app = app
        pass
