from haydovchi import Haydovchi
from time_gp import Time

class GP:
    def __init__(self, gp_name) -> None:
        self._gp_name = gp_name
        self.gp_drivers: list[Haydovchi] = []

    def get_gp_ranking(self):
        filterdict = {}
        for haydovchi in self.gp_drivers:
            driver_time: Time = haydovchi.time
            filterdict[haydovchi.ismi] = driver_time.second
        return sorted(filterdict.items(), key=lambda x:x[1])

    def add_driver(self, driver:Haydovchi):
        self.gp_drivers.append(driver)

    def __eq__(self, __value: object) -> bool:
        return self._gp_name == __value._gp_name

    @property
    def gp(self):
        return self._gp_name

    