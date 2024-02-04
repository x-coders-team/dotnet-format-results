from actions.Action import Action
from pprint import pprint
from inspect import getmembers

class CreateReportAction(Action):
    exampleService = None
    fileJsonEncoderService = None
    gitHubChecksService = None

    def __init__(self, app):
        super().__init__(app)
        self.exampleService = self.injectService('ExampleService')
        self.fileJsonEncoderService = self.injectService('FileJsonEncoderService')
        self.gitHubChecksService = self.injectService('GitHubChecksService')

    def exec(self):
        json_input = self._app.getArgumentByName('json_input')
        documentsCollection = self.fileJsonEncoderService.loadDocumentCollestionFromText(json_input)
        #pprint(documentsCollection)
        
        htmlOutput = self.exampleService.createSampleText(json_input)

        print(htmlOutput)
        pass
