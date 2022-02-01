from shop.apple import Apple
from shop.order import generate_order, Order
from shop.potato import Potato


def run_homework():

    ligol = Apple(species_name="ligol", size="L", price_per_kg=1.5)
    szara_reneta = Apple(species_name="Szara reneta", size="L", price_per_kg=3.5)
    print(f"4 kg ligola kosztuje {ligol.price_calculator(quantity=4)} pln.")
    print(f"2 kg szarej renety kosztuje {szara_reneta.price_calculator(quantity=2)} pln.")


    old_potato = Potato(species_name="Old potato", size="S", price_per_kg=0.8)
    print(f"10kg starego ziemniaka kosztuje {old_potato.price_calculator(quantity=10)} pln.")





if __name__ == '__main__':
    run_homework()

# DONE!