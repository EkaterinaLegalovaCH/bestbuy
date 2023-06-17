"""
create a class Product
with parametrs: name, price and quantity,
and methods such as set quantity, show info about
product, add product, remove product,
and so on
"""
class Product:

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def get_quantity(self):
        if self.quantity == 0:
            self.deactivate()
        return float(self.quantity)

    def set_quantity(self, quantity):
        self.quantity = quantity
        if self.quantity > 0:
            self.activate()

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

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
