#   Курс: AI+Python
#   Модуль 6. Функції
#   Тема: Функції. Частина 5

# Завдання 1
#   Напишіть lambda-функції, які:
#    Множить число на -1
#    Перевіряє чи рядок непорожній

# а) Множить число на -1
multiplication = lambda x: x * -1
print("\tМноження числа")
try:
    num = float(input("Введіть число: "))
    print(f"Число {num} при множенні на -1 = {multiplication(num)}")
except ValueError:
    print("Некоректний ввід!")


# b) Перевірка рядка на його заповненість
not_empty = lambda x: x != ""
print("\n\tПеревірка рядка")
text = input("Заповніть рядок: ")

if not_empty(text):
    print("Рядок заповнений!")
else:
    print("Рядок порожній!")

# Завдання 2
#   Напишіть функцію, яка використовуючи filter:
#    Отримує список чисел, рахує середнє арифметичне та повертає список з числами, які більші за середнє
#    Отримує список слів та повертає список слів, в яких рівно 4 літери


# а) Функція зі списком чисел більші за середнє
def numbers_average(numbers: list) -> list:
    average = sum(numbers) / len(numbers)
    result = list(filter(lambda x: x > average, numbers))
    return result


variable = [15, 20, 15, 30, 40]
print("\nСписок чисел, які більші за середнє: ", *numbers_average(variable))


# а) Функція зі списком слів в яких 4 літери
def four_letter(words: list) -> list:
    return list(filter(lambda x: len(x) == 4, words))


words = ["Valery", "Sofia", "Alyona", "Ivan", "Maria", "Guest", "Fine"]
print("Список слів в яких рівно 4 літери: ", *four_letter(words))

# Завдання 3
#   Напишіть функцію, яка отримує літеру та список слів і
#   знаходить слово зі списку, в якому найбільша кількість даної літери.


def count_letter(letter: str, words: list) -> list:
    if not words:
        return []

    count_max = max(word.count(letter) for word in words)

    if count_max == 0:
        return []

    return list(filter(lambda word: word.count(letter) == count_max, words))


words = [
    "Valery",
    "Lyudmila",
    "Vera",
    "Suzanna",
    "Ihor",
    "Svetlana",
    "Elena",
    "Sergey",
    "Alyona",
    "Ivan",
    "Maria",
]
letter = "a"

print(
    f"\nСлова зі списку в яких літера '{letter}' найбільше зустрічається, це: ",
    *count_letter(letter, words),
)
