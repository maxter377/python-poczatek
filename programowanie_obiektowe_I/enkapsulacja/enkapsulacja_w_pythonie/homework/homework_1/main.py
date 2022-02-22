from shop.order import Order
from shop.order_element import OrderElement
from shop.product import Product
from shop.order import generate_order


def run_homework():
    first_order = generate_order()
    print(first_order)

    cookie = Product(name="Ciastko", category_name="Jedzenie", unit_price=4)
    first_order.add_product_to_order_price(cookie, quantity=10)
    print(first_order)



if __name__ == '__main__':
    run_homework()

# DONE!