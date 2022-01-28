# class Student:
#
#     # Konstruktor zostanie wywołany podczas tworzenia obiektu
#     def __init__(self):
#         print("Powstaje nowy obiekt!")
#
# if __name__ == '__main__':
#     student = Student()

# class Student:
#
#     # Tak działa domyślny konstruktor
#     def __init__(self):
#         pass
#
# if __name__ == '__main__':
#     student = Student()



# class Student:
#
#     # Zadaniem konstruktora jest zdefiniować i zainicjalizować stan obiektu
#     def __init__(self):
#         self.first_name = "Maksiu"
#         self.last_name = "Sitek"
#         self.age = 26
#
#
# def run_example():
#     student = Student()
#     # # Do stanu obiektu mamy dostęp - możemy go odczytać
#     # print(student.first_name)
#     # print(student.last_name)
#     # print(student.age)
# #     Stan obiektu możemy zmodyfikować
#     student.first_name = "Jakub"
#     student.last_name = "Kowalski"
#     student.age = "30"
#     print(student.first_name)
#     print(student.last_name)
#     print(student.age)
#
#
# if __name__ == '__main__':
#     run_example()

class Student:

    # Konstruktor może przyjąć argumenty
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.promoted = False


# Obiekty możemy przekazywać jako argumenty do funkcji
def print_student(student):
    print(f"Student: {student.first_name} {student.last_name}, promoted: {student.promoted}")


# W funkcji możemy zmodyfikować stan obiektu (side effect)
def promote_student(student):
    student.promoted = True


def run_example():
    student = Student(first_name="Ola", last_name="Nowak")
    print_student(student)

    other_student = Student("Jerzy", "Jurkowski")
    print_student(other_student)

    promote_student(student)
    print_student(student)



if __name__ == "__main__":
    run_example()


