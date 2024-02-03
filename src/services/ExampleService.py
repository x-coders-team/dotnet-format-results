from services.ServiceAbstract import ServiceAbstract

class ExampleService(ServiceAbstract):
    def __init__(self, di={}, app=None):
        super().__init__(di, app)

    def createSampleText(self, jsonInput):
        return f"<html><head><title>Testing from Python</title></head><body><p>Testing workflow</p><div>{jsonInput}</div></body></html>"
