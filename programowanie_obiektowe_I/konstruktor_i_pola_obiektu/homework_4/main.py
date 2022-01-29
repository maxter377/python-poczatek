from shop.apple import Apple
from shop.order import generate_order, print_order
from shop.potato import Potato


def run_homework():
    green_apple = Apple(species_name="Green", size="M", price_per_kg=3.5)
    red_apple = Apple(species_name="Red", size="S", price_per_kg=2.8)
    print(green_apple.species_name, green_apple)
    print(red_apple.species_name, red_apple)

    old_potato = Potato(species_name="Potato old", size="S", price_per_kg=1.20)
    print(old_potato.species_name, old_potato)

    first_order = generate_order()
    print_order(first_order)
    second_order = generate_order()
    print_order(second_order)


if __name__ == '__main__':
    run_homework()

# DONE!