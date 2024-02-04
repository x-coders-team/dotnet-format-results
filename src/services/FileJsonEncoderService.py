from services.ServiceAbstract import ServiceAbstract
from models import DotnetFormatChange, DotnetFormatProjectId, DotnetFormatDocumentId, DotnetFormatDocument
import json
from pprint import pprint
from inspect import getmembers

class FileJsonEncoderService(ServiceAbstract):
    mapperService = None

    def __init__(self, di = None, app = None):
        super().__init__(di, app)
        self.mapperService = self.injectService('MapperDotnetFormatService')

    def loadDocumentCollestionFromText(self, documentCollestionText):
        documentsCollection = []
        rawData = json.loads(documentCollestionText)

        #pprint(rawData);

        documentsCollection = self.mapperService.mapDocumentsCollectionFromJson(rawData)

        return documentsCollection
    
    