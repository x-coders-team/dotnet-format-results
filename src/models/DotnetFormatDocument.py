class DotnetFormatDocument():
    _documentId = None
    _fileName = ''
    _filePath = ''
    _fileChanges = []

    def __init__(
        self, 
        documentId,
        fileName,
        filePath,
        fileChanges = []
    ):
        self._documentId = documentId
        self._fileName = fileName
        self._filePath = filePath
        self._fileChanges = fileChanges
        pass

    def getDocumentId(self):
        return self._documentId
    
    def getFileName(self):
        return self._fileName
    
    def getFilePath(self):
        return self._filePath
    
    def getFileChanges(self):
        return self._fileChanges
