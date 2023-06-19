"""
create a class Product
with parametrs: name, price and quantity,
and methods such as set quantity, show info about
product, add product, remove product,
and so on
"""
class Product:

    def __init__(self, name, price, quantity):
        try:
            if name == "":
                raise ValueError("Name of product can't be an empty string")
            self.name = name
        except ValueError as e:
            print("Error: ", str(e))
            self.name = None
        try:
            if price <= 0:
                raise ValueError("Price should be > 0")
            self.price = price
        except ValueError as e:
            print("Error: ", str(e))
            self.price = 0
        try:
            if quantity <= 0:
                raise ValueError("Quantity should be > 0")
            self.quantity = quantity
        except ValueError as e:
            print("Error: ", str(e))
            self.quantity = 0
        self.active = True

    def get_quantity(self):
        if self.quantity == 0:
            return self.deactivate()
        return float(self.quantity)

    def set_quantity(self, quantity):
        self.quantity = quantity
        if self.quantity > 0:
            return self.activate()
        else:
            return self.deactivate()

    def activate(self):
        self.active = True
        return self.active

    def deactivate(self):
        self.active = False
        return self.active

    def is_active(self):
        return self.active

    def show(self):
        print(f"{self.name}, Price: {self.price}, Quantity: {self.quantity}")

    def buy(self, quantity):
        try:
            if self.quantity >= quantity or quantity <= 0 or self.active is False:
                self.quantity -= quantity
                purchase = quantity * self.price
                if self.quantity == 0:
                    self.deactivate()
                return purchase
            else:
                raise Exception("Sorry, chosen quantity bigger than exist!")
        except Exception as e:
            print(e)
            return str(e)




