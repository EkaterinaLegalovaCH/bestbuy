import products
import store

# setup initial stock of inventory
product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                products.Product("Google Pixel 7", price=500, quantity=250)
                ]
best_buy = store.Store(product_list)
print(best_buy)

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
