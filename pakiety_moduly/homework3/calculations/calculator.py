def calculator(initial_capital, percentage, time):
    value = initial_capital * (1 + percentage / 100) ** time
    return value

