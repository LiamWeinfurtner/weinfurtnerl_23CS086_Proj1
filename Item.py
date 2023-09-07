class Item:
    
    def __init__(self, name, quantity, cost):
        self.name = name
        self.cost = cost
        self.quantity = quantity

    def __str__(self):
        return f"Item Name: {self.name}, Quantity: {self.quantity}, Cost: ${self.cost:.2f}"