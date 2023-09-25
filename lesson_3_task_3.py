from addresses import *
from mailing import *

track = int(randint(1000, 9999999))
cost = int(randint(150, 1000))
zip_code = int(randint(10000, 999999))
building = int(randint(1, 100))
apartment = int(randint(1, 50))

x= Mailing.item_mailing()

print(x)

