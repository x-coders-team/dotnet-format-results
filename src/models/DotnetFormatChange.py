class DotnetFormatChange():
    _lineNumber = ''
    _charNumber = ''
    _diagnosticId = ''
    _formatDescription = ''

    def __init__(
        self,
        lineNumber,
        charNumber,
        diagnosticId,
        formatDescription
    ):
        self._lineNumber = lineNumber
        self._charNumber = charNumber
        self._diagnosticId = diagnosticId
        self._formatDescription = formatDescription
        pass

    def getLineNumber(self):
        return self._lineNumber

    def getCharNumber(self):
        return self._charNumber

    def getDiagnosticId(self):
        return self._diagnosticId

    def getFormatDescription(self):
        return self._formatDescription
