"""
create a class Product
with parameters: name, price and quantity,
and methods such as set quantity, show info about
product, add product, remove product,
and so on
"""


class Product:

    def __init__(self, name, price, quantity, promotion):
        self.promotion = promotion
        self.order_quantity = 0
        self.promotion = None
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
            if quantity < 0:
                raise ValueError("Quantity should be >= 0")
            self.quantity = quantity
        except ValueError as e:
            print("Error: ", str(e))
            self.quantity = 0
        self.active = True
        self.promotion = None

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

    def set_promotion(self, promotion):
        self.promotion = promotion

    def buy(self, order_quantity):
        self.order_quantity = order_quantity
        try:
            if self.quantity >= self.order_quantity or self.order_quantity <= 0 or self.active is False:
                self.quantity -= self.order_quantity
                purchase = self.order_quantity * self.price - self.promotion.apply_promotion(self, self.order_quantity)
                if self.quantity == 0:
                    self.deactivate()
                return purchase
            else:
                raise Exception("Sorry, chosen quantity bigger than exist!")
        except Exception as e:
            print(e)
            return str(e)


class NonStockedProduct(Product):
    def __init__(self, name, price, promotion):
        super().__init__(name, price, quantity=0, promotion=promotion)
        self.promotion = promotion

    def buy(self, quantity):
        if self.promotion is not None:
            purchase = quantity * self.price - self.promotion.apply_promotion(self, quantity)
        else:
            purchase = quantity * self.price
        return purchase


class LimitedProduct(Product):
    def __init__(self, name, price, quantity, promotion):
        super().__init__(name, price, quantity, promotion)

    def buy(self, quantity):
        try:
            if self.quantity >= quantity or quantity <= 0 or self.active is False:
                self.quantity -= quantity
                purchase = quantity * self.price - self.promotion
                if self.quantity == 0:
                    self.deactivate()
                return purchase
            else:
                raise Exception("Sorry, chosen quantity is bigger than what is available!")
        except Exception as e:
            print(e)
            return str(e)
