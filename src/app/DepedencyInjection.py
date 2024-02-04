class DepedencyInjection():
    _di_services = []
    _service_module = 'services'

    def __init__(self, containers):
        self._di_services = containers
        pass

    def registryService(self, serviceName):
        if (len(self._di_services) == 0):
            self._di_services.append(dict())

        if self.isServiceExists(serviceName) == True:
            return
        
        module = __import__(self._service_module)
        serviceClass = getattr(module, serviceName)
        self._di_services[0][serviceName] = serviceClass(self)
        pass

    def isServiceExists(self, serviceName):
        if len(self._di_services) >  0: 
            if serviceName in self._di_services[0]:
                return True
            
        return False

    def getService(self, serviceName):
        self.registryService(serviceName)
        return self._di_services[0][serviceName]
