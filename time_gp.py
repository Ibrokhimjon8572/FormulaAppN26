class Time:
    def __init__(self, second) -> None:
        self._second = second

    @property
    def second(self):
        return self._second
