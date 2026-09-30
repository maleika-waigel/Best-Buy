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
        """Gibt die Menge (int) zurück."""
        return self.quantity


    def set_quantity(self, quantity):
        """
        Ändert die Menge.
        Wenn die Menge 0 erreicht, wird das Produkt deaktiviert.
        Wenn die Menge negativ ist, wird eine Exception ausgelöst.
        """
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")

        self.quantity = quantity

        if quantity == 0:
            self.active = False


    def is_active(self):
        """
        Gibt True zurück, wenn das Produkt aktiv ist, andernfalls False.
        """
        return self.active


    def activate(self):
        """Aktiviert das Produkt."""
        self.active = True


    def deactivate(self):
        """Deaktiviert das Produkt."""
        self.active = False


    def show(self):
        """
        Gibt einen String, der das Produkt repräsentiert, auf der Konsole aus.
        """
        print(f"{self.name}, Price: {self.price}, Quantity: {self.quantity}")


    def buy(self, quantity):
        """
        Kauft eine bestimmte Menge des Produkts.
        Gibt den Gesamtpreis (float) des Kaufs zurück.
        Aktualisiert die Produktmenge.
        """
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")
        elif quantity == 0:
            raise ValueError("Quantity must be at least 1")
        elif quantity > self.quantity:
            raise ValueError("Quantity not available")

        self.set_quantity(self.quantity - quantity)

        return self.price * quantity


bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
mac = Product("MacBook Air M2", price=1450, quantity=100)
