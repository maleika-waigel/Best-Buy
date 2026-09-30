import products


class Store:
    def __init__(self, list_of_products):
        self.list_of_products = list_of_products


    def add_product(self, product):
        """Fügt ein Produkt zum Store hinzu."""
        self.list_of_products.append(product)


    def remove_product(self, product):
        """Entfernt ein Produkt aus dem Store."""
        self.list_of_products.remove(product)


    def get_total_quantity(self):
        """
        Gibt zurück, wie viele Artikel insgesamt im Store vorhanden sind.
        """
        total_quantity = 0
        for product in self.list_of_products:
            total_quantity += product.get_quantity()
        return total_quantity


    def get_all_products(self):
        """Gibt alle Produkte im Store zurück, die aktiv sind."""
        active_products = []
        for product in self.list_of_products:
            if product.is_active():
                active_products.append(product)
        return active_products


    def order(self, shopping_list):
        """
        Erhält eine Liste von Tupeln, wobei jedes Tupel zwei Elemente enthält:
        - Produkt (Produktklasse) und
        - Menge (int).
        Kauft die Produkte und gibt den Gesamtpreis der Bestellung zurück.
        """
        total_price = 0
        for product, quantity in shopping_list:
            # print(product)
            # print(quantity)
            total_price += product.buy(quantity)
        return total_price



product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                products.Product("Google Pixel 7", price=500, quantity=250),
               ]

best_buy = Store(product_list)
products = best_buy.get_all_products()
print(best_buy.get_total_quantity())
print(best_buy.order([(products[0], 1), (products[1], 2)]))
