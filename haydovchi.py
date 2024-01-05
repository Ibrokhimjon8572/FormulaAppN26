class Haydovchi:
    def __init__(self, ismi) -> None:
        self._ismi = ismi
        self._time = None

    @property
    def ismi(self):
        return self._ismi
    
    @property
    def time(self):
        return self._time
    
    def set_time(self, value):
        self._time = value

    def __str__(self) -> str:
        return self.ismi