from shop.apple import Apple
from shop.order import generate_order, Order
from shop.potato import Potato


def run_homework():

    green_apple = Apple(species_name="Green apple", size="M", price_per_kg=2.5)
    szara_reneta = Apple(species_name="Szara Reneta", size="L", price_per_kg=4.5)


    print(green_apple)
    print(szara_reneta)



if __name__ == '__main__':
    run_homework()

# DONE!