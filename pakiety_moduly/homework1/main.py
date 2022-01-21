import Dystans

distance = int(input("Jaki dystans przebiegłeś? "))
time = int(input("W jakim czasie pokonałeś ten dystans? "))

dist = Dystans.avg_speed(distance, time)

print(f"Twoja średnia prędkość wynosi {dist:.2f} km/h.")