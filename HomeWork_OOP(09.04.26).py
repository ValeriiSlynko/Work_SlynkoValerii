# Курс: AI+Python
# Модуль 11. ООП
# Тема: ООП. Частина 5

#   ЗАВДАННЯ 1
#   Створіть клас Pet з атрибутами
#  name – ім’я тварини
#  satiety – рівень ситості(від 0 до 100, за замовчуванням 50)
#  energy – рівень енергії (від 0 до 100, за замовчуванням 50)

#   Методи:
#  sleep() – збільшує energy до 100
#  eat(food_amount) – їсть, збільшує satiety на food_amount
#  play(activity_level) – абстрактний метод
#  make_sound() – просто pass

#   Створіть клас Cat
#   Методи:
#  play(activity_level) – якщо satiety > 60, зменшує energy на 2 * activity_level та satiety на activity_level
#  make_sound() – виводить ‘Мяу’
#  catch_mouse() – якщо energy > 30, ловить мишу. Якщо satiety > 40, то грається з мишею, інакше їсть

#   Створіть клас Dog
#   Методи:
#  play(activity_level) – якщо satiety > 15, зменшує energy на activity_level//2 та satiety на activity_level//2
#  make_sound() – виводить ‘Гав’
#  fetch_ball() – ловить м’яча якщо satiety>10, зменшує energy на 5

from abc import ABC, abstractmethod

class Pet(ABC):

    def __init__(self, name, satiety = 50, energy = 50):
        # створюємо базові параметри
        self._name = name
        self._satiety = satiety
        self._energy = energy

    # метод створення ліміту ситості та енергії
    def _limit(self):
        self.satiety = max(0, min(100, self.satiety))
        self.energy = max(0, min(100, self.energy))

    # стан тварин
    def show_status(self):
        print(f"{self.name} має ситість: {self.satiety} та енергію: {self.energy}")

    # метод відновлення енергії через 'сон'
    def sleep(self):
        self.energy = 100
        self._limit()

    # метод збільшення ситості
    def eat(self, food_amount):
        self.satiety += food_amount
        self._limit()

    # абстрактний метод
    @abstractmethod
    def play(self, activity_level):
        pass

    @abstractmethod
    def make_sound(self):
        pass


class Cat(Pet):
    # метод, який показує ігри котика, якщо ситість 60 +
    def play (self, activity_level):
        if self.satiety > 60:
            self.energy -= 2 * activity_level
            self.satiety -= activity_level
            self._limit()

    # метод виводить 'Мяу'
    def make_sound(self):
        print('Мяу!')

    # метод показує, що котик ловить мишу, якщо енергія 30+
    def catch_mouse (self):
        if self.energy > 30:
            print(f"{self.name} - ловить мишу!")

            if self.satiety > 40:   # умова коли котик грається, а коли їсть мишу
                print(f"{self.name} - грається з мишею!")
            else:
                print(f"{self.name} - їсть мишу!")
        else:
            print(f"Котик {self.name} втомлений!")

class Dog(Pet):

    def play (self, activity_level):
        if self.satiety > 15:
            self.energy -= activity_level // 2
            self.satiety -= activity_level // 2
            self._limit()

    def make_sound(self):
        print('Гав!')

    def fetch_ball (self):
        if self.satiety > 10:
            print(f" Песик {self.name} - грається м'ячем!")
            self.energy -= 5
            self._limit()
        else:
            print(f" Песик {self.name} - дуже втомлений!")


# маємо список тварин
pets = [
    Cat("Мартин", 60, 80),
    Dog("Лорд", 30, 50),
    Cat("Сєня", 100, 40),
    Dog("Бім", 20, 90)
]

print("Початковий стан домашніх тварин\n")
for pet in pets:
    pet.show_status()

print("Дії тварин\n")
for pet in pets:
    pet.eat(10)
    pet.play(5)
    pet.make_sound()

print("Стан тварин після дій:\n")
for pet in pets:
    pet.show_status()
