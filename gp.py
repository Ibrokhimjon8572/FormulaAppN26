class GP:
    def __init__(self, gp_name) -> None:
        self._gp_name = gp_name

    @property
    def gp(self):
        return self._gp_name

    