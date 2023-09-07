from Vendor import Vendor
from Item import Item

machine = Vendor()
#FIXME: Not dispensing the one penny for some reason, need to look into it
machine.addItem("Chips", 3, 2.79)
print(machine.coins)
machine.buyItem("Chips", 2, 0, 0, 0, 0)
print(machine.coins)
