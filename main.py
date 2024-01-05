from chempionship import Chempionship
from time_gp import Time

chempionship = Chempionship()

gp1 = chempionship.create_gp("1kun1")

driver1 = chempionship.create_driver('ali')

time1 = Time(2341234)
driver2 = chempionship.create_driver('vali')
time2 = Time(2341236)

print(chempionship.set_time(gp1, driver1, time1))
print(chempionship.set_time(gp1, driver2, time2))

# ["ali", "vali"]

# print(chempionship.get_drivers())

# print(chempionship.get_driver('ali'))
# print(chempionship.get_driver('alis'))




# print()

