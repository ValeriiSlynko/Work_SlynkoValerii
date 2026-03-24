# ЗАВДАННЯ 2
# Напишіть функцію для обрахунку площі трикутника по
# формулі
#  S = 0,5 * a * b * sin(у)
# Параметри функції: сторони a і b та кут. Функцію синус візьміть з модуля -math-
# Примітка: якщо ви будете вводити кут у градусах, то перед тим як рахувати синус, його потрібно перевести у радіани.
# Див math.radians()

import math


def triangle_area(a: float, b: float, angle_deg: float) -> float:
    """
    Обчислюємо площу трикутника за формулою:
    S = 1/2 * a * b * sin(angle)

    angle_deg — кут у градусах
    """
    angle_rad = math.radians(angle_deg)  # переводимо в радіани
    area = 0.5 * a * b * math.sin(angle_rad)
    return area


print("Площа трикутника = ", triangle_area(5, 6, 45))

# ЗАВДАННЯ 3
# Напишіть функцію, яка обчислює суму чисел від 1 до 10 млн. Виведіть час роботи програми.
# Див time.time()
import time


def calculate_sum():
    total = 0
    for i in range(1, 10_000_001):
        total += i
    return total


start_time = time.time()

result = calculate_sum()

end_time = time.time()

print("Сума:", result)
print("Час виконання:", end_time - start_time, "секунд")

# ЗАВДАННЯ 4
# Користувач вводить свою дату народження у форматі YYYY-MM-DD. Виведіть вік користувача.
# Див datetime.date.fromisoformat()
#  datetime.date.today()
#  datetime.timedelta.days

import datetime


def calculate_age(birth_date_str: str) -> int:
    """
    Обчислює вік користувача в роках.
    Формат дати: YYYY-MM-DD
    """

    birth_date = datetime.date.fromisoformat(birth_date_str)
    today = datetime.date.today()

    delta = today - birth_date
    age = delta.days // 365  # приблизно

    return age


user_input = input("Введіть дату народження (YYYY-MM-DD): ")
print("Ваш вік:", calculate_age(user_input))
