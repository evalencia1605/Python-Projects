class Item:
    def __init__(self, name: str, price: int, quantity: int):
        #Run validations
        assert price >= 0, f"Price {price} is not greater than zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater than zero!"
        
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price * self.quantity


item1 = Item("IPhone", 1600, 5)
print(item1.calculate_total_price())

item2 = Item("Laptop", 2100, 3)
print(item2.calculate_total_price())



