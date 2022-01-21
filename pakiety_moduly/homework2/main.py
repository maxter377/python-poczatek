import math

def calculate_c_len(a, b):
    c = math.sqrt(math.pow(a, 2) + math.pow(b, 2))
    return c

a = float(input("Jaka jest długość boku a? "))
b = float(input("Jaka jest długość boku b? "))

c = calculate_c_len(a, b)
print(f"Długość przeciwprostokątnej to {c}")