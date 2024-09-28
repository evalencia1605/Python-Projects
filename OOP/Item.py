class Item:
    def __init__(self, name):
        print(f"An instance created: {name}")
           
    def calculate_total_price(self, x, y):
        return x * y


item1 = Item("IPhone")
item1.name = "IPhone"
item1.price = 1200
item1.quantity = 5
print(item1.calculate_total_price(item1.price, item1.quantity))

item2 = Item("Laptop")
item2.name = "IPhone"
item2.price = 2100
item2.quantity = 3
print(item2.calculate_total_price(item2.price, item2.quantity))



