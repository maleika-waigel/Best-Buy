class Product:
    def __init__(self, name, price, quantity):
        """
        - Konstruktor-Methode.
        - Wenn etwas ungültig ist (leerer Name / negativer Preis oder Menge), wird eine Ausnahme ausgelöst.
        - Erstellt die Instanzvariablen (aktiv wird auf True gesetzt).
        """
        if price < 0:
            raise ValueError("Price cannot be negative")
        if not name:
            raise ValueError("Name cannot be empty")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True


    def get_quantity(self):
        """
        Getter-Methode für die Menge.
        Gibt die Menge (int) zurück.
        """
        pass

    def set_quantity(self, quantity):
        """
        Setter-Methode für die Menge. Wenn die Menge 0 erreicht,
        wird das Produkt deaktiviert.
        """
        pass

    def is_active(self):
        """
        Getter-Methode für aktiv.
        Gibt True zurück, wenn das Produkt aktiv ist, andernfalls False.
        """
        pass

    def activate(self):
        """Aktiviert das Produkt."""
        pass

    def deactivate(self):
        """Deaktiviert das Produkt."""
        pass

    def show(self):
        """
        Gibt einen String, der das Produkt repräsentiert, auf der Konsole aus, z.B.:
        "MacBook Air M2, Price: 1450, Quantity: 100"
        """
        pass

    def buy(self, quantity):
        """
        Kauft eine bestimmte Menge des Produkts.
        Gibt den Gesamtpreis (float) des Kaufs zurück.
        Aktualisiert die Produktmenge.
        Bei Problemen (wann? darüber nachdenken), wird eine Ausnahme ausgelöst.
        """
        pass


bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
mac = Product("MacBook Air M2", price=1450, quantity=100)

"""
print(bose.buy(50))
print(mac.buy(100))
print(mac.is_active())

bose.show()
mac.show()

bose.set_quantity(1000)
bose.show()
"""