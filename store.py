"""
created a class Store,
take a list of objects class Product as a parameter.
"""
class Store:
    def __init__(self, list_of_products):
        self.list_of_products = list_of_products
        self.total_quantity = 0
        self.list = []

    def add_product(self, product):
        self.list_of_products.append(product)
        print(self.list_of_products)

    def remove_product(self, product):
        self.list_of_products.remove(product)
        print(self.list_of_products)

    def get_total_quantity(self):
        for product in self.list_of_products:
            self.total_quantity += product.get_quantity()
        return self.total_quantity

    def get_all_products(self):
        n = 0
        for product in self.list_of_products:
            if product.is_active() is True:
                n += 1
                print(f"{n}. ", end="")
                product.show()
        for product in self.list_of_products:
            product_info = {}
            product_info["name"] = product.name
            product_info["price"] = product.price
            product_info["quantity"] = product.quantity
            if product.active is True:
                self.list.append(product_info)
        return self.list

    def order(self):
        self.total_price = 0
        print("When you want to finish order, enter empty text.")
        while True:
            item_buy = input("Which product # do you want? ")
            self.amount_buy = input("What amount do you want? ")
            if item_buy == "" or self.amount_buy == "":
                break
            purchase = self.list_of_products[int(item_buy) - 1].buy(int(self.amount_buy))
            try:
                self.total_price += purchase * int(self.amount_buy)
                print("Product added to list!")
            except TypeError:
                print()
        return f"Order made! Total payment: ${self.total_price}"
