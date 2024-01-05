from haydovchi import Haydovchi
from gp import GP
from time_gp import Time


class Chempionship:
    def __init__(self) -> None:
        self.driver_list:list[Haydovchi] = []
        self.gp_list:list[GP] = []

    def set_time(self, gp:GP, driver:Haydovchi, time:Time):
        driver.set_time(time)
        for inner_gp in self.gp_list:
            if inner_gp == gp:
                inner_gp.add_driver(driver)
                return time
        return None
        
    def create_gp(self, gp_name):
        gp = GP(gp_name)
        self.gp_list.append(gp)
        return gp
    
    def get_gp(self, gp_name):
        for gp in self.gp_list:
            if gp.gp == gp_name:
                return gp
        return None

    def create_driver(self, ismi):
        haydovchi = Haydovchi(ismi)
        self.driver_list.append(haydovchi)
        return haydovchi
    
    def get_drivers(self):
        return self.driver_list
    
    def get_driver(self, driver_name):
        for driver in self.driver_list:
            if driver.ismi == driver_name:
                return driver
        return None

