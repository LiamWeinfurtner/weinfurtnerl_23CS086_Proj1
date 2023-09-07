"""
Commands: 
 - balance
 - history
 - inventory
 - add item <str> <int> <float>
 - buy item <str> {5}<int>
 - help
 - exit
"""

from Item import Item

class Vendor:

    def __init__(self): # Extra money each vendor object starts with
        self.coins = {
            'Pennies' : 25,
            'Nickels' : 10,
            'Dimes'   : 5,
            'Quarters': 4,
            'Dollars' : 10
        }

        # Will store each valid command the user inputs
        self.commandHistory = []

        # Will store each item that is added to the machine
        self.inventory = []

    def calculateTotalMoney(self, dollars, quarters, dimes, nickels, pennies):
        total = dollars*1 + quarters*.25 + dimes*.10 + nickels*.05 + pennies*.01
        return total
    
        """Searches for an item in the Vendor's inventory. If found, returns that item object. If not found, returns None.
        """
    def fetchItem(self, itemName):
        for item in self.inventory:
            if item.name == itemName:
                return item
        return None

    def addItem(self, name, quantity, cost):
        self.inventory.append(Item(name, quantity, cost))

    def calculateChange(self, cost, dollars, quarters, dimes, nickels, pennies):
        # Calculate the total amount of money provided
        total_money = self.calculateTotalMoney(dollars, quarters, dimes, nickels, pennies)

        # Calculate the change needed
        change = total_money - cost

        # Initialize variables to store the number of each denomination in the change
        change_dollars = 0
        change_quarters = 0
        change_dimes = 0
        change_nickels = 0
        change_pennies = 0

        # Calculate the change in the most efficient way
        while change >= 1.00:
            change_dollars += 1
            change -= 1.00

        while change >= 0.25:
            change_quarters += 1
            change -= 0.25

        while change >= 0.10:
            change_dimes += 1
            change -= 0.10

        while change >= 0.05:
            change_nickels += 1
            change -= 0.05

        while change >= 0.00:
            change_pennies += 1
            change -= 0.01

        return {
            'Dollars' : change_dollars,
            'Quarters': change_quarters,
            'Dimes'   : change_dimes,
            'Nickels' : change_nickels,
            'Pennies' : change_pennies
        }

    # FIXME: Need to add a check against whether or not there is enough change to give back to customer
    def buyItem(self, itemName, dollars, quarters, dimes, nickels, pennies):
        moneyTotal = self.calculateTotalMoney(dollars, quarters, dimes, nickels, pennies)

        # Check if item exists
        item = self.fetchItem(itemName)
        if item.name == None:
            print("No such item. Please try again.")
        # Check if item is in stock
        elif item.quantity <= 0:
            print("Insufficent item.")
        # Check if money deposited is enough to buy item
        elif moneyTotal < item.cost:
            print("Insufficient funds. Please supply more money in order to purchase " + itemName)
        # Buy item, add in change if there is any to the vendor, and subtract item from inventory
        else:
            # Deposit customer money
            self.coins['Dollars']  += int(dollars)
            self.coins['Quarters'] += int(quarters)
            self.coins['Dimes']    += int(dimes)
            self.coins['Nickels']  += int(nickels)
            self.coins['Pennies']  += int(pennies)

            # If change is needed, calculate if the required change exists
            changeRequired = self.calculateChange(item.cost, dollars, quarters, dimes, nickels, pennies)
            if (changeRequired['Dollars'] < self.coins['Dollars'] | changeRequired['Quarters'] < self.coins['Quarters'] | changeRequired['Dimes'] 
            < self.coins['Dimes'] | changeRequired['Nickels'] < self.coins['Nickels'] | changeRequired['Pennies'] < self.coins['Pennies']):
                print("This machine does not have enough change, whoops. Try again later maybe.")
                # Dispense customer money again
                self.coins['Dollars']  -= int(dollars)
                self.coins['Quarters'] -= int(quarters)
                self.coins['Dimes']    -= int(dimes)
                self.coins['Nickels']  -= int(nickels)
                self.coins['Pennies']  -= int(pennies)
            else:
                print("Funds accepted, dispensing " + itemName + ". Thank you for your purchase.")
                # Dispense customer change
                print(changeRequired)
                self.coins['Dollars']  -= int(changeRequired["Dollars"])
                self.coins['Quarters'] -= int(changeRequired["Quarters"])
                self.coins['Dimes']    -= int(changeRequired["Dimes"])
                self.coins['Nickels']  -= int(changeRequired["Nickels"])
                self.coins['Pennies']  -= int(changeRequired["Pennies"])
                self.fetchItem(itemName).quantity -= 1
