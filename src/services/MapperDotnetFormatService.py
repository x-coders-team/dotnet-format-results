from services.ServiceAbstract import ServiceAbstract
from models import DotnetFormatChange, DotnetFormatProjectId, DotnetFormatDocumentId, DotnetFormatDocument
from pprint import pprint
from inspect import getmembers

class MapperDotnetFormatService(ServiceAbstract):
    def __init__(self, di = None):
        """The MapperDotnetFormatService class is responsible for mapping raw data transformed from a JSON string 
           into a list of objects in the MapperDotnetFormatService format. This service encapsulates the logic for transforming
           JSON data into a specific format defined by the MapperDotnetFormatService, providing a convenient and reusable way
           to process and work with data in a standardized manner.

        Args:
            di (DepedencyInjection, optional): _description_. Defaults to None.
        """

        super().__init__(di)

    def mapDocumentsCollectionFromJson(self, rawData):
        """Maps a collection of documents from raw JSON data to an array of objects in the DotnetFormatDocument format.

        Args:
            rawData (List): An array returned from an external source in JSON format containing document data.

        Returns:
            List: An array of objects representing the transformed documents in the DotnetFormatDocument format.
        """

        documentsCollection = []

        for rawDocument in rawData:
            documentsCollection.append(self._createDocument(rawDocument))

        return documentsCollection
    
    def _createDocument(self, rawDocument):
        """Private function that creates and returns an array of DotnetFormatDocument objects
           from an associative array retrieved from an external source in JSON format.

        Args:
            rawDocument (dict): An associative array containing raw document data in JSON format.

        Returns:
            DotnetFormatDocument: objects representing the transformed documents in the DotnetFormatDocument format.
        """

        documentId = self._createDocumentId(rawDocument['DocumentId'])

        return DotnetFormatDocument(
            documentId = documentId,
            fileName = rawDocument['FileName'],
            filePath = rawDocument['FilePath'],
            fileChanges = self._createChangesCollection(rawDocument['FileChanges'])
        )
    
    def _createDocumentId(self, rawDocumentId):
        """Private function that creates and returns a DotnetFormatDocumentId object
           from an associative array retrieved from an external source in JSON format.

        Args:
            rawDocumentId (Dict): An associative array containing raw document ID data in JSON format.

        Returns:
            DotnetFormatDocumentId: An object representing the transformed document ID in the DotnetFormatDocumentId format.
        """

        return DotnetFormatDocumentId(
            projectId = self._createProjectId(rawDocumentId['ProjectId']),
            id = rawDocumentId['Id']
        )
    
    def _createProjectId(self, rawProjectId):
        """Private function that creates and returns a DotnetFormatProjectId object
           from an associative array retrieved from an external source in JSON format.

        Args:
            rawProjectId (Dict): An associative array containing raw project ID data in JSON format.

        Returns:
            DotnetFormatProjectId: An object representing the transformed project ID in the DotnetFormatProjectId format.
        """

        return DotnetFormatProjectId(id = rawProjectId['Id'])
    
    def _createChangesCollection(self, rawFileChanges):
        """Private function that creates and returns an array of DotnetFormatChange objects
           from an array of associative arrays retrieved from an external source in JSON format.

        Args:
            rawFileChanges (List[Dict[str, Any]]): An array of associative arrays containing raw file change data in JSON format.

        Returns:
            List: An array of objects representing the transformed file changes in the DotnetFormatChange format.
        """

        changesCollection = []

        for rawFileChange in rawFileChanges:
            changesCollection.append(self._createFileChange(rawFileChange))
            
        return changesCollection
    
    def _createFileChange(self, rawFileChange):
        """Private function that creates and returns a DotnetFormatChange object
           from an associative array retrieved from an external source in JSON format.

        Args:
            rawFileChange (Dict): An associative array containing raw file change data in JSON format.

        Returns:
            DotnetFormatChange: An object representing the transformed file change in the DotnetFormatChange format.
        """

        return DotnetFormatChange(
            lineNumber = rawFileChange['LineNumber'],
            charNumber = rawFileChange['CharNumber'],
            diagnosticId = rawFileChange['DiagnosticId'],
            formatDescription = rawFileChange['FormatDescription']
        )
    