class DotnetFormatDocumentId():
    _projectId = None
    _id = ''

    def __init__(self, projectId, id):
        self._projectId = projectId
        self._id = id
        pass

    def getProjectId(self):
        return self._projectId

    def getId(self):
        return self._id
