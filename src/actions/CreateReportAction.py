from actions.Action import Action

class CreateReportAction(Action):
    exampleService = None
    
    def __init__(self, app):
        super().__init__(app)
        self.exampleService = self._app.getService('ExampleService')

    def exec(self):
        json_input = self._app.getArgumentByName('json_input')
        htmlOutput = self.exampleService.createSampleText(json_input)
        print(htmlOutput)
        pass
