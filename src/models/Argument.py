class Argument():
    def __init__(self, name, value):
        self._name = name
        self._value = value
        pass
    
    def getName(self):
        return self._name
    
    def getValue(self):
        return self._value
    