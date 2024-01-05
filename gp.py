from haydovchi import Haydovchi

class GP:
    def __init__(self, gp_name) -> None:
        self._gp_name = gp_name
        self.gp_drivers: list[Haydovchi] = []

    def add_driver(self, driver:Haydovchi):
        self.gp_drivers.append(driver)

    def __eq__(self, __value: object) -> bool:
        return self._gp_name == __value._gp_name

    @property
    def gp(self):
        return self._gp_name

    