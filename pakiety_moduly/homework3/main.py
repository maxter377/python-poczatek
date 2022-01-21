import calculations.calculator

def ask_for_int_value(message):
    input_value = input(message)
    return int(input_value)



initial_capital = ask_for_int_value("Jaka jest początkowa wartość kapitału? ")
percentage = ask_for_int_value("Jaki jest procent? ")
time = ask_for_int_value("Jaki jest czas trwania lokaty? ")

final_value = calculations.calculator.calculator(initial_capital, percentage, time)
print(f"Po {time} latach Twoja lokata będzie warta {final_value:.2f}")