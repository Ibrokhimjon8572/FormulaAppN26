class Haydovchi:
    def __init__(self, ismi) -> None:
        self._ismi = ismi
        self.time = None

    @property
    def ismi(self):
        return self._ismi
    
    def set_time(self, value):
        self.time = value
        
    def __str__(self) -> str:
        return self.ismi