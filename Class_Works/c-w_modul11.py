# Курс: AI+Python
# Модуль 11. ООП
# Тема: ООП. Частина 1
from unicodedata import name


#   Завдання 1
# Створіть клас Student з атрибутами name та age.
# Додайте метод для виводу інформації у форматі «Ім’я: {name}, вік: {age}»

print("Створюємо клас Student з атрибутами для виводу інформації у форматі «Ім’я: {name}, вік: {age}»")
class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def student_info (self):
        print(f"Ім'я студента: {self.name}, Його вік: {self.age} років")

student_1 = Student (name= "Ахіллес", age = 40 )

student_1.student_info()


#   Завдання 2
# Створіть список з 3-ма студентами, дані вводить користувач.
# Після чого для кожного студента виведіть інформацію про нього за допомогою метода.

print("\nСтворюємо список 3-х студентів з виводом інформації про них!")

class Student():

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_info (self):
        print(f"Ім'я студента: {self.name}, Його вік: {self.age}")

student_1 = Student (name= "Валерій", age = 37 )
student_2 = Student (name= "Роман", age = 38 )
student_3 = Student (name= "Стас", age = 39 )

students = []

students.append(student_1)
students.append(student_2)
students.append(student_3)

for student in students:
    student.show_info()


#    Завдання 3
# Створіть клас Circle з атрибутом radius.
# Додайте метод для отримання площі кола

print("\nСтворюємо клас Circle з атрибутом radius та отримуємо площі колів")

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_area_circle(self):
        return math.pi * self.radius ** 2

circle_1 = Circle(radius = 15)
circle_2 = Circle(radius = 25)

print(f"Радіус 1-го кола = " , round(circle_1.get_area_circle(),2))
print(f"Радіус 2-го кола = " , round(circle_2.get_area_circle(),2))


#   Завдання 4
# Створіть клас BankAccount з атрибутами owner та balance.
# Додайте метод deposit для поповнення рахунку
# Додайте метод withdraw для зняття грошей з рахунку
# Додайте метод info для виведення інформації про баланс

print("\nСтворюємо клас BankAccount з атрибутами owner та balance для клієнтів")

class BankAccount:

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):

        if amount > 0:
            self.balance += amount
        else:
            print(f" {self.owner} : Ви не можете внести від'ємну суму")

    def withdraw(self, amount):
        if 0 < amount < self.balance:
            self.balance -= amount

    def info(self):
        print(f"{self.owner} : Баланс {self.balance} S")

client_1 = BankAccount("Валерій", 1000)
client_2 = BankAccount("Євген", 800)
client_3 = BankAccount("Богдан" ,1200)

client_1.deposit(1500)
client_2.info()
client_3.withdraw(1000)
client_1.info()

#   Завдання 5
# Створіть клас Car з атрибутами brand(марка), year(рік випуску), is_ready(чи готовий до поїздки, за замовчування False).
# Додайте метод start_engine який заводить двигун, і змінює атрибут is_ready
# Додайте метод move який виводить повідомлення, що автомобіль їде, або ж ще не готовий в залежності від is_ready.

print("\nСтворюємо клас Car з атрибутами brand(марка), year(рік випуску), is_ready(чи готовий до поїздки")

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
