class Apple:

    def __init__(self, species_name, size, price_per_kg):
        self.species_name = species_name
        self.size = size
        self.price_per_kg = price_per_kg

    def price_calculator(self, quantity):
        return quantity * self.price_per_kg