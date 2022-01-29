
class Product:
    def __init__(self, name, category_name, unit_price):
        self.name = name
        self.category_name = category_name
        self.unit_price = unit_price



class Order:
    def __init__(self, client_first_name, client_last_name, products=None):
        self.client_first_name = client_first_name
        self.client_last_name = client_last_name
        if products is None:
            products = []
        self.products = products

        total_price = 0
        for product in products:
            total_price += product.unit_price
        self.total_price = total_price




class Apple:
    def __init__(self, species_name, size, price_per_kg):
        self.species_name = species_name
        self.size = size
        self.price_per_kg = price_per_kg



class Potato:
    def __init__(self, species_name, size, price_per_kg):
        self.species_name = species_name
        self.size = size
        self.price_per_kg = price_per_kg


def run_homework():
    green_apple = Apple(species_name="Green", size="M", price_per_kg=3.5)
    red_apple = Apple(species_name="Red",size="S", price_per_kg=2.8)
    print(green_apple.species_name, green_apple)
    print(red_apple.species_name, red_apple)

    old_potato = Potato(species_name="Potato old", size="S", price_per_kg=1.20)
    print(old_potato.species_name, old_potato)

    cookies = Product(name="Cookies", category_name="Food", unit_price=4)
    empty_order = Order(client_first_name="Maksiu", client_last_name="Sitek")
    order = Order(client_first_name="Fernando", client_last_name="Alonso", products=[cookies])
    print(cookies)
    print(empty_order)
    print(order)

if __name__ == '__main__':
    run_homework()




