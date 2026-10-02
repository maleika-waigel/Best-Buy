import products
import store

SEPARATOR = "=============================="


def display_products(store_instance):
    """Gibt alle aktiven Produkte des Stores mit Nummer aus."""
    all_products = store_instance.get_all_products()
    print(SEPARATOR)

    for number, product in enumerate(all_products, start=1):
        print(number, end=". ")
        product.show()

    print(f"{SEPARATOR}\n")


def make_order(store_instance):
    """
    Ermöglicht dem Benutzer, eine Bestellung aus mehreren
    Produkten zusammenzustellen.
    """
    display_products(store_instance)
    print("When you want to finish order, enter empty text.\n")

    order_list = []

    while True:
        all_products = store_instance.get_all_products()

        order = input("Which product # do you want? ")
        amount = input("What amount do you want? ")

        if not order or not amount:
            break

        try:
            order = int(order)
            amount = int(amount)
        except ValueError:
            print("Error adding product!\n")
            continue

        if 0 < order <= len(all_products):
            order_list.append((all_products[order - 1], amount))
            print("Product added to list!\n")
        else:
            print("Error adding product!\n")
            continue

    if order_list:
        try:
            total_amount = store_instance.order(order_list)
            print("\n********")
            print(f"Order made! Total payment: ${total_amount}")
        except ValueError:
            print("Error while making order! Quantity larger than what exists")


def start(store_instance):
    """Startet das Store-Menü und verarbeitet die Benutzereingaben."""
    while True:
        print("\nStore Menu")
        print("----------")
        print()
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")
        print()

        try:
            choice = int(input("Please choose a number: "))
            print()
        except ValueError:
            print("Error with your choice! Try again!")
            continue

        if choice == 1:
            display_products(store_instance)

        elif choice == 2:
            print(SEPARATOR)
            print(f"Total of {store_instance.get_total_quantity()} items in store")
            print(SEPARATOR)

        elif choice == 3:
            make_order(store_instance)

        elif choice == 4:
            return

        else:
            print("Invalid input")


# Anfangsbestand des Stores erstellen
product_list = [ products.Product("MacBook Air M2", price=1450, quantity=100),
                 products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                 products.Product("Google Pixel 7", price=500, quantity=250)
               ]
best_buy = store.Store(product_list)


def main():
    """Startet das Programm."""
    start(best_buy)


if __name__ == "__main__":
    main()
