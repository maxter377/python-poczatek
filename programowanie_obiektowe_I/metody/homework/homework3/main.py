from shop.apple import Apple
from shop.order import generate_order, Order
from shop.potato import Potato


def run_homework():

    first_order = generate_order()

    second_order = generate_order()


    print(f"Liczba elementów w 1 zamówieniu to: {len(first_order)}")
    print(f"Liczba elementów w 2 zamówieniu to: {len(second_order)}")


if __name__ == '__main__':
    run_homework()

# DONE!