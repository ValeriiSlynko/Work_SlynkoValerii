# Курс: AI+Python
# Модуль 11. ООП
# Тема: ООП. Частина 1
from lamda import name

#   Завдання 1
# Створіть клас Student з атрибутами name та age. Додайте
# метод для виводу інформації у форматі «Ім’я: {name}, вік: {age}»

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

Student.student_info(name="Ахілес", age="40")

#   Завдання 2
# Створіть список з 3-ма студентами, дані вводить користувач.
# Після чого для кожного студента виведіть інформацію про нього за допомогою метода.

class Student():

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def student_info (self):
        print(f"Ім'я: {self.name}, Вік: {self.age}")

student_1 = Student (name= "Валерій", age = 37 )
student_2 = Student (name= "Глєб", age = 38 )
student_3 = Student (name= "Джек", age = 39 )

students = []

students.append(student_1)
students.append(student_2)
students.append(student_3)

for student in students:
    student.student_info()

print(students)


#    Завдання 3
# Створіть клас Circle з атрибутом radius.
# Додайте метод для отримання площі кола

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def circumference(self):
        return math.pi * self.radius ** 2

circle = Circle(radius = 5)
circle_1 = Circle(radius = 10)

print(circle.radius)

#   Завдання 4
# Створіть клас BankAccount з атрибутами owner та balance.
# Додайте метод deposit для поповнення рахунку
# Додайте метод withdraw для зняття грошей з рахунку
# Додайте метод info для виведення інформації про баланс

class BankAccount:

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):

        if amount > 0:
            self.balance += amount
        else:
            print(f" {self.owner} : ")

    def withdraw(self, amount):
        if amount > 0 and amount < self.balance:
            self.balance -= amount

    def balances(self):
        pass

client_1 = BankAccount("Валерій")


#   Завдання 5
# Створіть клас Car з атрибутами brand(марка), year(рік випуску), is_ready(чи готовий до поїздки, за замовчування False).
# Додайте метод start_engine який заводить двигун, і змінює атрибут is_ready
# Додайте метод move який виводить повідомлення, що автомобіль їде, або ж ще не готовий в залежності від is_ready.

class Car:

    def __init__(self, brand, year):
        self.brand = brand
        self.year = year
        self.is_ready = False

    def start_engine(self):
        print(f"Двигун {self.brand} заводиться!")
        self.is_ready = True

    def move(self):

        if self.is_ready:
            print(f"Автомобіль {self.brand} вже їде")
        else:
            print(f"Автомобіль {self.brand} ще не готовий!")

auto_1 = Car("Тойота", 2025)
auto_2 = Car("Ауді", 2023)

auto_1.start_engine()
auto_1.move()

auto_2.move()
auto_2.start_engine()
