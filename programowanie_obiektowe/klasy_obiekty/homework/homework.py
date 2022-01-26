if __name__ == '__main__':

    class Product:
        pass

    class Order:
        pass

    class Apple:
        pass

    class Potato:
        pass

    ligol = Apple()
    antonowka = Apple()
    szara_reneta = Apple()

    ziemniak = Potato()
    frytki = Potato()
    czipsy = Potato()

    print("ligol type::", type(ligol))
    print("antonowka type:", type(antonowka))
    print("szara reneta type::", type(szara_reneta))

    print("ziemniak type", type(ziemniak))
    print("frytki type:", type(frytki))
    print("czipsy type:", type(czipsy))


    orders = [Order(), Order(), Order(), Order(), Order()]

    print(orders)

    products = {
        "Jabłko": Product(),
        "Ziemniak": Product(),
        "Marchew": Product(),
        "Ciastka": Product(),
    }

    print(products)
