from shop.order import Order
from shop.order_element import OrderElement
from shop.product import Product
from shop.order import generate_order


def run_homework():
    order_over_limit = generate_order(30)
    # print(order_over_limit)

    cookie = Product(name="Ciasteczko", category_name="Jedzenie", unit_price=4.5)
    # order_below_limit = generate_order(15)
    # order_below_limit.add_product_to_order_price(cookie, quantity=10)
    # print(order_below_limit)
    order_over_limit.add_product_to_order_price(cookie, quantity=10)
    # print(order_over_limit)


if __name__ == '__main__':
    run_homework()

# DONE!