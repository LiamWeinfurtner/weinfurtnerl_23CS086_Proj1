from Vendor import Vendor
from Item import Item

# Instantiate the vending machine
machine = Vendor()

# Add two items to begin with
machine.addItem("Mountain_Dew", 5, 2.99)
machine.addItem("Coke_Zero", 3, 3.19)

# Create user input loop
while True:
    # Display a prompt and get user input
    user_input = input("Enter a command or type 'Help' for a list of commands (or 'exit' to quit): ")
    user_input = user_input.lower()
    user_input_split = user_input.split()
    
    # Check if the user wants to exit the loop
    if user_input == "exit":
        print("Thank you for shopping with us!")
        break  # Exit the loop

    # Process the user commands
    if user_input == "balance":
        machine.displayBalance()
        machine.commandHistory.append(user_input)
        
    elif user_input == "history":
        machine.displayHistory()
        machine.commandHistory.append(user_input)
        
    elif user_input == "inventory":
        if len(machine.inventory) == 0:
            print("There are no items in this vendor's inventory, sorry!")
        else:
            machine.displayInventory()
            machine.commandHistory.append(user_input)
            
    elif user_input == "help":
        print("Commands")
        print("balance")
        print("    - Shows vendor balance")
        print("history")
        print("    - Shows command history")
        print("inventory")
        print("    - Shows vendor inventory and prices")
        print("add item <name str> <qty int> <price float>")
        print("    - Add an item to the vendor inventory")
        print("buy item <name str> <dollars int> <quarters int> <dimes int> <nickels int> <pennies int>")
        print("    - Buys an item with dollars, quarters, dimes, nickels, and pennies. Dispenses change.")
        print("help")
        print("    - Prints a help menu with these commands")
        print("exit")
        print("    - Exit the console")
        machine.commandHistory.append(user_input)
                  
    elif (len(user_input_split) == 5):
        if (user_input_split[0] == "add") & (user_input_split[1] == "item"):
            newItem = machine.parseItemAdd(user_input)
            machine.addItem(newItem[0], newItem[1], newItem[2])
            machine.commandHistory.append(user_input)
            
    elif (len(user_input_split) == 8):
        if (user_input_split[0] == "buy") & (user_input_split[1] == "item"):
            buyItem = machine.parseItemBuy(user_input)
            # If format not wrong, buyItem
            if buyItem != None:
                machine.buyItem(buyItem[0], buyItem[1], buyItem[2], buyItem[3], buyItem[4], buyItem[5])
                machine.commandHistory.append(user_input)
            
    else:
        print("Error. Invalid command. Please try again.")

