# Модуль 11. ООП
# Тема: ООП. Частина 3

#   ЗАВДАННЯ 1
# Створіть наступні класи:
#  Rectangle – атрибути width, height
#  Circle – атрибути radius
#  Triangle – атрибути a, b, c
# Методи:
#  get_perimeter()
#  display_info()
# Напишіть функцію create_figure() яка запитує у користувача
# тип фігури та потрібні атрибути і повертає об’єкт.
# Створіть декілька фігур, добавте їх у список та для кожної викличте відповідні методи.

import math

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_perimeter(self):
        return 2 * (self.width + self.height)

    def display_info(self):
        print(f"Прямокутник: ширина={self.width}, висота={self.height}")


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_perimeter(self):
        return 2 * math.pi * self.radius

    def display_info(self):
        print(f"Коло: радіус={self.radius}")


class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def get_perimeter(self):
        return self.a + self.b + self.c

    def display_info(self):
        print(f"Трикутник: сторони={self.a}, {self.b}, {self.c}")

def create_figure():
    figure_type = input("Тип фігури (rectangle / circle / triangle): ").lower()

    if figure_type == "rectangle":
        width = float(input("Ширина: "))
        height = float(input("Висота: "))
        return Rectangle(width, height)

    elif figure_type == "circle":
        radius = float(input("Радіус: "))
        return Circle(radius)

    elif figure_type == "triangle":
        a = float(input("Сторона a: "))
        b = float(input("Сторона b: "))
        c = float(input("Сторона c: "))
        return Triangle(a, b, c)

    else:
        print("Невідомий тип фігури")
        return None

figures = []

# for _ in range(3):  # створимо 3 фігури
#     fig = create_figure()
#     if fig:
#         figures.append(fig)
#
# print("\nІнформація про фігури:")
#
# for f in figures:
#     f.display_info()
#     print(f"Периметр: {f.get_perimeter():.2f}")


#   ЗАВДАННЯ 2
# Створіть наступні класи:
#  Manager – атрибути name, base_salary
#  Developer – атрибути name, base_salary, work_experience
#  Inter – атрибути name, base_salary
# Методи:
#  get_salary() – менеджер отримує базову ставку,
#
# розробник отримує на 20% більше якщо стаж більше 4
# років, інтерн отримує половину базової ставки
# Напишіть функцію create_worker() яка запитує у
# користувача тип працівника та потрібні атрибути і повертає об’єкт.
# Створіть декілька співробітників, добавте їх у список та для
# кожного викличте відповідні методи.

class Manager:

    def __init__(self, name: str, base_salary: float):
        self._name = name
        self._base_salary = base_salary

    def get_salary(self) -> float:
        return self._base_salary

class Developer:

    def __init__(self, name: str, base_salary: float, work_experience: int):
        self._name = name
        self._base_salary = base_salary
        self._work_experience = work_experience

    def get_salary(self) -> float:

        if self._work_experience > 4:
            return self._base_salary * 1.2
        return self._base_salary

class Intern:
    def __init__(self, name: str, base_salary: float):
        self._name = name
        self._base_salary = base_salary

    def get_salary(self) -> float:
        return self._base_salary * 0.5

def create_worker() -> Manager | Developer | Intern | None:
    worker_type = input("Введіть тип працівника (manager, developer, intern): ").lower()

    name = input("Ім'я: ")
    base_salary = float(input("Базова зарплата: "))

    if worker_type == "manager":
        return Manager(name, base_salary)

    elif worker_type == "developer":
        exp = int(input("Стаж роботи (роки): "))
        return Developer(name, base_salary, exp)

    elif worker_type == "intern":
        return Intern(name, base_salary)

    else:
        print("Невідомий тип даних!")
        return None

workers = []

# створюємо працівників в кількості - 3
# for _ in range(3):
#     worker = create_worker()
#
#     if worker:
#         workers.append(worker)
#
# for worker in workers:
#     print(f"{worker.get_salary()}")


#   ЗАВДАННЯ 3
# Створіть наступні класи:
#  Car – атрибути speed
#  Bicycle – атрибути speed
#  Boat – атрибути speed
#   Методи:
#  move() – виводить повідомлення про рух
#   Car – їде по шосе зі швидкістю
#   Bicycle – їде по дорозі зі швидкістю
#   Boat – пливе по воді зі швидкістю
#   check_speed(speed) – перевіряє чи правильна швидкість,
# якщо ні, то в __init__ треба викикати ValueError з відповідним повідомленням
#  - Car – від 20 до 200
#  - Bicycle – від 10 до 30
#  - Boat – від 0 до 50
# Напишіть функцію create_vehicle() яка запитує у користувача тип транспорту та потрібні атрибути і повертає об’єкт.
# Створіть декілька транспортних засобів, добавте їх у список та для кожної викличте відповідні методи.

class Car:
    def __init__(self, spead: float):
        self.check_speed(spead)
        self.speed = spead

    def check_speed(self, speed: float):
        if speed < 20 or speed > 200:
            raise ValueError ("Швидкість авто має бути в межах від 20 до 200 км/год")

    def move(self):
        print(f"Авто їде зі швидкістю {self.speed}")

class Bicycle:
    def __init__(self, speed: float):
        self.check_speed(speed)
        self.speed = speed

    def check_speed(self, speed: float):
        if speed < 10 or speed > 30:
            raise ValueError ("Швидкість велосипеда має бути в межах від 10 до 30 км/год")

    def move(self):
        print(f"Велосипед їде по дорозі зі швидкістю {self.speed}")

class Boat:
    def __init__(self, speed: float):
        self.check_speed(speed)
        self.speed = speed

    def check_speed(self, speed: float):
        if speed < 0 or speed > 50:
            raise ValueError ("Швидкість човна має бути в межах від 0 до 50 км/год")

    def move(self):
        print(f"Човен пливе по воді зі швидкістю {self.speed}")

def create_vehicle() -> Car | Bicycle | Boat | None:
    vehicle_type = input("Оберіть тип транспорту (Car/Bicycle/Boat): ").lower()

    try:
        speed = float (input("Швидкість транспорту: "))

        if vehicle_type == "car":
            return Car(speed)

        elif vehicle_type == "bicycle":
            return Bicycle(speed)

        elif vehicle_type == "boat":
            return Boat(speed)

        else:
            print("Невідомий тип транспорту!")
            return None

    except ValueError as Error:
        print(f"Помилка: {Error}")
        return None

vehicles = []

for _ in range(3):
    vehicle = create_vehicle()

    if vehicle:
        vehicles.append(vehicle)

for vehicle in vehicles:
    vehicle.move()
