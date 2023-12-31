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
from decimal import *

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
        """Calculates the total sum in dollars and cents given dollars and coin denominations.

        Args:
            dollars (Int): Number of dollars.
            quarters (Int): Number of quarters.
            dimes (Int): Number of dimes.
            nickels (Int): Number of nickels.
            pennies (Int): Number of pennies.

        Returns:
            Double: The total value in dollars and cents.
        """
        total = round(dollars*1, 2) + round(quarters*.25, 2) + round(dimes*.10,2 ) + round(nickels*.05, 2) + round(pennies*.01, 2)
        return total
    
    def fetchItem(self, itemName):
        """Searches for an item in the Vendor's inventory. If found, returns that item object. If not found, returns None.

        Args:
            itemName (String): Name of item to search for.

        Returns:
            Item: Item object if found, None if not.
        """
        for item in self.inventory:
            if item.name.lower() == itemName:
                return item
        return None

    def addItem(self, name, quantity, cost):
        """Adds a new item to the inventory of the vendor.

        Args:
            name (String): Name of the item.
            quantity (Int): Quantity of item being added.
            cost (Double): Cost of the item.
        """
        
        if self.fetchItem(name) != None:
            print("Item already exists.")
            return
        
        self.inventory.append(Item(name, quantity, cost))
        print("Item successfully added.")

    def calculateChange(self, cost, dollars, quarters, dimes, nickels, pennies):
        """Calculates the number of coins in change required given a cost and customer deposited money.

        Args:
            cost (Double): Cost of the item being bought.
            dollars (Int): Number of dollars deposited by customer.
            quarters (Int): Number of quarters deposited by customer.
            dimes (Int): Number of dimes deposited by customer.
            nickels (Int): Number of nickels deposited by customer. 
            pennies (Int): Number of pennies deposited by customer.

        Returns:
            Library: Contains the number of dollars, quarters, dimes, nickels, and pennies owed to the customer.
        """
        
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

    def buyItem(self, itemName:str, dollars:int, quarters:int, dimes:int, nickels:int, pennies:int):
        """Purchases an item from the vendor if it exists, the customer has enough money, and the vendor can dispense the appropriate amount of change.

        Args:
            itemName (String): Name of item to be bought.
            dollars (Int): Number of dollars customer deposists.
            quarters (Int): Number of quarters customer deposists.
            dimes (Int): Number of dimes customer deposists.
            nickels (Int): Number of nickels customer deposists.
            pennies (Int): Number of pennies customer deposists.
        """
        moneyTotal = self.calculateTotalMoney(dollars, quarters, dimes, nickels, pennies)

        # Check if item exists
        item = self.fetchItem(itemName)
        if item == None:
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
                print("Funds accepted, dispensing " + itemName + ". Here is your change:")
                print(changeRequired)
                # Dispense customer change, subtract from vendor balance
                self.coins['Dollars']  -= int(changeRequired["Dollars"])
                self.coins['Quarters'] -= int(changeRequired["Quarters"])
                self.coins['Dimes']    -= int(changeRequired["Dimes"])
                self.coins['Nickels']  -= int(changeRequired["Nickels"])
                self.coins['Pennies']  -= int(changeRequired["Pennies"])
                self.fetchItem(itemName).quantity -= 1

    def displayBalance(self):
        """Prints amount of dollars and coins stored in the vendor.
        """
        print(self.coins)
        
    def displayHistory(self):
        """Prints the user's command history.
        """
        max_length = max(len(s) for s in self.commandHistory)
        print("+-" + "-" * max_length + "-+")
        for s in self.commandHistory:
            print(f"| {s:{max_length}} |")
        print("+-" + "-" * max_length + "-+")
        
    def displayInventory(self):
        # Determine the maximum lengths of name, quantity, and cost for formatting
        max_name_length = max(len(max([item.name for item in self.inventory], key=len)), len("Name"))
        max_quantity_length = max(len(max([str(item.quantity) for item in self.inventory], key=len)), len("Quantity"))
        max_cost_length = max(len(max([f"${item.cost:.2f}" for item in self.inventory], key=len)), len("Cost"))
        
        # Header row for the table
        header = f"| {'Name':<{max_name_length}} | {'Quantity':>{max_quantity_length}} | {'Cost':>{max_cost_length}} |"
        separator = "+-" + "-" * max_name_length + "-+-" + "-" * max_quantity_length + "-+-" + "-" * max_cost_length + "-+"
        
        # Print the table header
        print(separator)
        print(header)
        print(separator)

        # Print each item in the table
        for item in self.inventory:
            cost_formatted = f"${item.cost:.2f}"
            row = f"| {item.name:<{max_name_length}} | {item.quantity:>{max_quantity_length}} | {cost_formatted:>{max_cost_length}} |"
            print(row)

        # Print the table footer
        print(separator)
        
    def parseItemAdd(self, inputString):

        # Split the input string into words
        words = inputString.split()

        # Check if the input has the correct format
        if len(words) != 5 or words[0] != 'add' or words[1] != "item":
            print("Invalid input format. Use 'add item <str> <int> <float>'.")
            return

        try:
            name = words[2]
            quantity = int(words[3])
            cost = float(words[4])

            # Check data type validation
            if not isinstance(name, str) or not isinstance(quantity, int) or not isinstance(cost, float):
                print("Invalid input format. Use 'add item <str> <int> <float>'.")
                return

            return name, quantity, cost

        except (ValueError, IndexError):
            raise ValueError("Invalid input format or data types.")
        
        
    def parseItemBuy(self, inputString):
        
        # Split the input string into words
        words = inputString.split()
        
        # Check if the input has the correct format
        if len(words) != 8 or words[0] != "buy" or words[1] != "item":
            print("Invalid input format or item does not exist. Use 'buy item <str> <int> <int> <int> <int> <int>")
            return
        
        try:
            name = words[2]
            dollars = int(words[3])
            quarters = int(words[4])
            dimes = int(words[5])
            nickels = int(words[6])
            pennies = int(words[7])
            
            # Check data type validation
            if not isinstance(name, str) or not isinstance(dollars, int) or not isinstance(quarters, int) or not isinstance(dimes, int) \
                or not isinstance(nickels, int) or not isinstance(pennies, int):
                    print("Invalid coin input format. Please enter the number of dollars, quarters, dimes, nickels, and pennies as integers.")
                    return None
                
            # Check if someone decided to be funny and use negatives
            if dollars < 0 or quarters < 0 or dimes < 0 or nickels < 0 or pennies < 0:
                print("Please enter positive values for your demoninations.")
                return None
            
            return name, dollars, quarters, dimes, nickels, pennies
        
        except (ValueError, IndexError):
            raise ValueError("Invalid input format or data types.")
            
            