import products
import store
import promotions

# setup initial stock of inventory
product_list = [products.Product("MacBook Air M2", price=1450, quantity=100, promotion=None),
                products.Product("Bose QuietComfort Earbuds", price=250, quantity=500, promotion=None),
                products.Product("Google Pixel 7", price=500, quantity=250, promotion=None),
                products.NonStockedProduct("Windows License", price=125, promotion=None),
                products.LimitedProduct("Shipping", price=10, quantity=250, promotion=None)
                ]
best_buy = store.Store(product_list)

# Create promotion catalog
second_half_price = promotions.SecondHalfPrice("Second Half price!")
third_one_free = promotions.ThirdOneFree("Third One Free!")
thirty_percent = promotions.PercentDiscount("30% off!", percent=30)

# Add promotions to products
product_list[0].set_promotion(second_half_price)
product_list[1].set_promotion(third_one_free)
product_list[3].set_promotion(thirty_percent)


def start(my_store):
    """
    Take a created object class Store
    as a parameter,
    and run a menu with choice of actions
    until quit
    """
    while True:
        print("""
Store Menu:
-----------
1. List all products in store
2. Show total  amount in store
3. Make an order
4. Quit
    """)
        choice = input("Please, choose a number: ")
        if choice == "1":
            my_store.get_all_products()
        elif choice == "2":
            print(my_store.get_total_quantity())
        elif choice == "3":
            print(my_store.order())
        elif choice == "4":
            break


def main():
    start(best_buy)


if __name__ == "__main__":
    main()
