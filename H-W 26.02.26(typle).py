# Курс: AI+Python
# Модуль 7. Кортежі, множини, словники
# Тема: Кортежі. Частина 1

# Завдання 1
# Є кортеж з назвами міст. Виведіть ті міста, які зустрічаються в кортежі більше одного разу.

name_city = (
    "Kharkiv",
    "Kyiv",
    "Odessa",
    "Lviv",
    "Dnipro",
    "Poltava",
    "Kharkiv",
    "Kyiv",
)

duplicate = []

for city in name_city:
    if name_city.count(city) > 1 and city not in duplicate:
        duplicate.append(city)

print("Міста, що найчастіше зустрічаються: ", duplicate)


# Завдання 2
# Є два кортежі з випадковими числами. Виведіть на екран ті числа, які є в першому кортежі, але немає в другому.
import random

tuple_1 = tuple(random.randint(1, 15) for _ in range(8))
tuple_2 = tuple(random.randint(1, 15) for _ in range(8))

print("\nНабір чисел у першому кортежі: ", tuple_1)
print("Набір чисел у другому кортежі: ", tuple_2)

result = []

for numeric in tuple_1:
    if numeric is not tuple_2:
        result.append(numeric)

print("\nСписок чисел, які є ТІЛЬКИ в першому кортежі: ", result)

# Завдання 3
# Напишіть функцію, яка отримує 2 кортежі.
# Поверніть список з елементами, які є в обох кортежах і мають однакові індекси.
# Підказка: використайте zip()


def similar_elements(tuple_num_1: tuple, tuple_num_2: tuple) -> list:
    result = []

    for a, b in zip(tuple_num_1, tuple_num_2, strict=False):
        if a == b:
            result.append(a)

    return result


tuple_num_1 = (
    1,
    3,
    5,
    7,
    9,
    11,
    12,
    13,
    14,
    15,
)  # створено вручну, але можна через "import random"
tuple_num_2 = (
    2,
    4,
    6,
    8,
    10,
    11,
    12,
    13,
    14,
    15,
)  # створено вручну, але можна через "import random"

print("\nПерший кортеж: ", tuple_1)
print("Другий кортеж: ", tuple_2)
print(
    "Список однакових елементів та індексів по кортежах: ",
    similar_elements(tuple_num_1, tuple_num_2),
)
