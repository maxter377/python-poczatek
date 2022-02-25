# import random
#
#
# class Student:
#
#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.promoted = False
#
#     def __bool__(self):
#         return self.promoted
#
#
# def run_example():
#     student = Student(first_name="Maksiu", last_name="Sitek")
#     print(bool(student))
#
#     student.promoted = True
#     print(bool(student))
#
#     if student:
#         print("If student")
#
#     student.promoted = False
#     if student:
#         print("If student")
#
#
# if __name__ == '__main__':
#     run_example()

# -------------------------------
# poniżej mamy przykład gdy nie zaimplementujemy 4_metody bool a spróbujemy ją wywołać

import random


class Student:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.promoted = False


class School:

    def __init__(self, name, students):
        self.name = name
        self.students = students

    def __len__(self):
        return len(self.students)


def create_school_with_students(school_name):
    number_of_students = random.randint(1, 20)
    students = []
    for student_number in range(number_of_students):
        first_name = f"Student-{student_number}"
        last_name = "Smith"
        students.append(Student(first_name, last_name))

    school = School(school_name, students)
    return school

def run_example():
    school = create_school_with_students("Hogwart")
    # school.students = []
    # jak powyższe odkomentujemy to bedzie FALSE bo długość (len) listy studentów będize 0
    print(bool(school))


if __name__ == '__main__':
    run_example()
#
# JEŻELI ZAIMPLEMENTUJEMY METODE LEN TO:
# Wynik będzie True bo zawsze generuje się lista studentów o długości co najmniej 1 (bo mamy 1-20)

# JEŚLI NIE ZAIMPLEMENTUJEMY ANI LEN ANI BOOL
# Python uzna zawsze za true