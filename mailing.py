from random import randint
from addresses import *
class Mailing:
    to_address = None
    from_address = None

    def __init__(self, track, cost, code, buildings, apartment):
        self.track = track
        self.cost = cost
        self.code = code
        self.building = buildings
        self.apartment = apartment


     def item_mailing(self):
         self.Address(self.code, self.building, self.apartment)
         self.to_address = Address.get_address()
         self.from_address = Address.get_address()
         return (self.to_address, self.from_address, self.track, self.cost)




