# Курс: AI+Python
# Модуль 8. Файли. Винятки
# Тема: Винятки. Частина 1
# Завдання 1
# Є список з товарами. Користувач вводить індекс товару,
# який треба вивести. Обробіть виняток

goods = ["Комп'ютер", "Стілець", "Стіл", "Шафа", "Світильник"]

try:
    index_good = int(input("Введіть індекс товару: "))
    print(f"Товар під індексом {index_good}", "-", goods[index_good])

except ValueError:
    print("Введіть ціле число!")
except IndexError:
    print("Ви ввели не існуючий індекс!")


# Завдання 2
# Напишіть функцію, яка запитує користувача вік та повертає його.
# Якщо вік неправильний(<0 або >130) викликати виняток ValueError.
# Написати код try … except який використовує дану функцію.


def user_age():
    age = int(input("\nВведіть вік користувача: "))

    if age <= 0 or age > 130:
        raise ValueError("Вік не може бути менше 0 або більше 130 років")

    return age


try:
    age = user_age()
    print(f"Ваш вік: {age} років!")

except ValueError as err:
    print(f"ПОМИЛКА! {err}")

# Завдання 3
# Напишіть функцію, яка запитує користувача номер телефону та повертає його.
# Якщо номер не вірний, тобто не починається з +380 або в ньому не 13 символів то викликати виняток ValueError.
# Написати код try … except який використовує дану функцію.


def user_phone_number():
    phone_numbers = input("\nВведіть Ваш номер телефону: ")

    if phone_numbers[:4] != "+380":
        raise ValueError("Номер телефону не починається із коду '+380' !")

    if len(phone_numbers) != 13:
        raise ValueError("Введений номер повинен містити 11 символів!")

    return phone_numbers


try:
    phone_numbers = user_phone_number()
    print("Ви ввели номер телефону: ", phone_numbers)

except ValueError as err:
    print("ПОМИЛКА!", err)


# Завдання 4
# Організуйте фільтр товарів в онлайн магазині.
# Усі товари діляться на певні категорії, причому один і той самий товар може відноситись до різних категорій.
# Є словник, де ключі – назви категорій, а значення – множини з товарами цієї категорії.
# Користувач вводить 2 категорії, виведіть ті товари, які відносяться одночасно до цих двох категорій.
# Обробіть виняток коли категорії немає в словнику.
# Додатково: змініть код якщо користувач вводить декілька категорій.

online_shop = {
    "Електроніка": {"Телефони", "Ноутбуки", "Планшети"},
    "Дім": {"Стіл", "Стільці", "Ноутбуки"},
    "Офіс": {"Принтер", "Стільці", "Ноутбуки"},
}

try:
    category_1 = input("\nВведіть 1-шу категорію: ")
    category_2 = input("Введіть 2-гу категорію: ")

    result = online_shop[category_1] & online_shop[category_2]
    print("Спільні товари: ", ", ".join(result) if result else "Немає")

except KeyError:
    print("Такої категорії не існує")

# ВАРІАНТ коду, якщо користувач ХОЧЕ побачити спілні товари з декількох категорій
print(
    "\nВАРІАНТ КОДУ коли користувач вводить декілька категорій і бачить спільні товари!"
)

online_shop_1 = {
    "Електротовари": {"Телефони", "Ноутбуки", "Планшети"},
    "Дім": {"Стіл", "Стільці", "Ноутбуки"},
    "Офіс": {"Принтер", "Стільці", "Ноутбуки"},
}

try:
    categories = input("Введіть категорії через кому: ").split(",")

    # очищаємо пробіли
    categories = [cat.strip() for cat in categories]

    # беремо першу множину
    result = online_shop_1[categories[0]]

    # перетин з іншими
    for cat in categories[1:]:
        result = result & online_shop[cat]

    print("Спільні товари:", ", ".join(result) if result else "немає")

except KeyError as e:
    print(f"Категорії '{e.args[0]}' не існує")

# Завдання 5
# Організуйте базу даних «Співробітники».
# Усі дані мають зберігатись у словнику де ключ – ім’я людини, значення – зарплата.
# Реалізуйте такий функціонал(через функції):
#  Вивести дані на екран
#  Добавити співробітника
#  Видалити співробітника
#  Показати зарплату співробітника
#  Змінити зарплату співробітнику
# У випадку некоректних даних функції повинні викликати винятки з описом помилки

# employees = {
#     "Валерій": 50000,
#     "Альона": 40000
# }
#
#
# def show_all(data: dict) -> None:
#     if not data:
#         print("База даних порожня!")
#         return
#
#     for name, salary in data.items():
#         print(f"{name}: {salary}")
#
# def add_employee(data: dict, name: str, salary: int) -> None:
#     if name in data:
#         raise ValueError("Такий співробітник вже існує!")
#
#     if salary < 0:
#         raise ValueError("Зарплата не може бути від'ємною!")
#
#     data[name] = salary
#
#
# def remove_employee(data: dict, name: str) -> None:
#     if name not in data:
#         raise KeyError("Такого співробітника не знайдено")
#
#     del data[name]
#
#
# def get_salary(data: dict, name: str) -> int:
#     if name not in data:
#         raise KeyError("Такого співробітника не знайдено")
#
#     return data[name]
#
#
# def update_salary(data: dict, name: str, new_salary: int) -> None:
#     if name not in data:
#         raise KeyError("Такого співробітника не знайдено")
#
#     if new_salary < 0:
#         raise ValueError("Зарплата не може бути від'ємною")
#
#     data[name] = new_salary
#
#
# try:
#     add_employee(employees, "Іван", 30000)
#     print("Додано співробітника: Іван")
#
#     update_salary(employees, "Валерій", 60000)
#     print("Оновлено зарплату для: Валерій")
#
#     salary = get_salary(employees, "Валерій")
#     print(f"Зарплата співробітника Валерій: {salary}")
#
#     remove_employee(employees, "Альона")
#     print("Видалено співробітника: Альона")
#
#     print("\nСписок співробітників:")
#     show_all(employees)
#
# except (ValueError, KeyError) as err:
#     print(f"ПОМИЛКА: {err}")
