from Vendor import Vendor
from Item import Item

# Instantiate the vending machine
machine = Vendor()

# Add two items to begin with
machine.addItem("Mountain Dew", 5, 2.99)
machine.addItem("Coke Zero", 3, 3.19)

# Create user input loop
while True:
    # Display a prompt and get user input
    user_input = input("Enter a command (or 'exit' to quit): ")
    user_input = user_input.lower()
    user_input_split = user_input.split()
    
    # Check if the user wants to exit the loop
    if user_input == "exit":
        print("Thank you for shopping with us.")
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
        print("I need the help, not you")
                  
    elif (len(user_input_split) == 5):
        if (user_input_split[0] == "add") & (user_input_split[1] == "item"):
            newItem = machine.parseItemAdd(user_input)
            machine.addItem(newItem[0], newItem[1], newItem[2])
            machine.commandHistory.append(user_input)
            
    #FIXME: Need to add the buy item command
    #FIXME: I need to check for add item duplicates
    #FIXME: Check for spaces in add item and buy item name strings
    #FIXME: I think spaces for all names are just going to have to be underscores, limit user to underscores
    #FIXME: Fix the dang help menu to be formatted nicely somehow
    
    else:
        print("Error. Invalid command. Please try again.")

