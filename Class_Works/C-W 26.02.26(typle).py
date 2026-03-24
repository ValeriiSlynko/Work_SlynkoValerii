# Курс: AI+Python
# Модуль 7. Кортежі, множини, словники
# Тема: Кортежі. Частина 1

# Завдання 1
# Користувач вводить числа через кому. Збережіть їх у кортеж.
# Виведіть на екран:
#  Суму чисел
#  Найбільше та найменше число
#  Перші та останні 3 числа
#  Кількість чисел 7
#  Пари індекс – число
# Додатково, якщо користувач введе порожній рядок, то
# створіть власний кортеж з випадковими числами(12 шт.).
import random

user = input("Введіть числа через кому: ")

if user == "":
    numbers = tuple(random.randint(1, 20) for _ in range(12))
    print("Створено рандомний кортеж:", numbers)
else:
    numbers_list = user.split(",")
    numbers_list = [int(x) for x in numbers_list]
    numbers = tuple(numbers_list)

# Сам кортеж
print("Кортеж:", numbers)

# Сума
print("Сума чисел:", sum(numbers))

# Найбільше та найменше числа
print("Найбільше число:", max(numbers))
print("Найменше число:", min(numbers))

# Перші та останні 3 числа
print("Перші 3 числа:", numbers[:3], "та останні 3 числа:", numbers[-3:])

# Кількість чисел 7
print("Кількість чисел 7: ", numbers.count(7))

# Пари індекс – число
print("Пари індекс – число: ")
for index, value in enumerate(numbers):
    print(index, "-", value)


# Завдання 2
# Напишіть наступну програму: є кортеж з іменами зареєстрованих студентів.
# Користувач вводить ім’я студента після чого отримує повідомлення, чи студент зареєстрований.
# Програма закінчує роботу коли користувач введе порожній рядок.

students = ("Valery", "Alyona", "Ivan", "Maria", "Sofia")

while True:
    name_student = str(input("Введіть ім'я студента для перевірки: "))

    if name_student == "":
        print("Введено порожній рядок! Програма закінчена .")
    elif name_student in students:
        print(f"Студент {name_student} зареєстрований.")
        break
    else:
        print(f"Студент {name_student} НЕ зареєстрований.")
        break

# Завдання 3
# Напишіть наступну програму: є кортеж з назвами фільмів.
# Користувач вводить назву фільму.
#  Якщо фільм знаходиться в першій половині кортежу, треба вивести ретро-фільм
#  Якщо в другій половині – сучасний фільм
#  Якщо один з останніх п'яти – новий фільм
movies = (
    "Titanic",
    "Gladiator",
    "The Matrix",
    "Forrest Gump",
    "The Godfather",
    "Avatar",
    "Inception",
    "Interstellar",
    "Joker",
    "Dune",
    "Oppenheimer",
    "Barbie",
)

film = str(input("Введіть назву фільму: "))

if film in movies:
    index = movies.index(film)
    middle = len(movies) // 2

    if film in movies[-5:]:
        print(f"{film} - Це новий фільм")
    elif index < middle:
        print(f"{film} - Це ретро-фільм")
    else:
        print(f"{film} - Це сучасний фільм")
else:
    print("Введений фільм не знайдено в списку.")

# Завдання 4
# Напишіть функцію, яка отримує кортеж з назвами фруктів та слово.
# Потрібно повернути скільки разів дане слово зустрічається в кортежі (регістр неважливий).
# Складні назви теж враховуються.
# Приклад: ("яблуко", "яблуко Сидоренко", "банан жовтий", "Яблуко")
# Яблуко зустрічається 3 рази


def count_fruit(fruits_tuple, word):
    count = 0
    word = word.lower()

    for fruit in fruits_tuple:
        if word in fruit.lower():
            count += 1
    return count


fruits = ("яблуко", "яблуко Сидоренко", "банан жовтий", "Яблуко")

result = count_fruit(fruits, "Яблуко")
print("Кількість входжень:", result)


# Завдання 5
# Напишіть функцію, яка отримує кортеж з числами та
# виводить на екран статистику по-кількості чисел з різною кількістю цифр.
# Приклад:
# одноцифрових – 3 шт.
# двоцифрових – 5 шт.
# трицифрових – 2 шт.


def number_statistics(numbers):
    one_digit = 0
    two_digit = 0
    three_digit = 0

    for num in numbers:
        length = len(str(abs(num)))

        if length == 1:
            one_digit += 1
        elif length == 2:
            two_digit += 1
        elif length == 3:
            three_digit += 1

    print("Одноцифрових –", one_digit, "шт.")
    print("Двоцифрових –", two_digit, "шт.")
    print("Трицифрових –", three_digit, "шт.")


# Завдання 6
# Користувач вводить назви товарів через кому. Потрібно сформувати кортеж.
# Також вводяться ціни товарів, які теж треба зберегти у кортеж. Виведіть на екран пари товар – ціна.
# Також виведіть назви найдорожчого та найдешевшого товарів.

print("\nВСТИГ за пару")
