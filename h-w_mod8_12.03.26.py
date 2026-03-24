# Курс: AI+Python
# Модуль 8. Файли. Винятки
# Тема: Винятки. Частина 1

#    ЗАВДАННЯ 1
# Напишіть функцію, яка запитує користувача пароль та повертає його.
# Якщо пароль поганий, тобто менше 8 символів чи містить однакові символи то викликати виняток ValueError.
# Написати код try … except який використовує дану функцію.


def user_parol():
    # запитуємо пароль у користувача
    password = input("Введіть свій пароль: ")

    # перевіряємо довжину
    password_len = len(password)
    print(f"Довжина пароля = {password_len} символів")

    # перевірка на повтори символів
    uniq_characters = set(password)
    print("Унікальні символи: ", uniq_characters)

    # умова поганого пароля
    if password_len < 8 or len(uniq_characters) < password_len:
        raise ValueError(
            "Пароль не може містити менше 8 символів або містити дублікати!"
        )
        # повертаємо пароль - якщо все добре
    return password


# виконуємо основний блок з обробкою винятків
try:
    user_password = user_parol()
    print(f"Пароль успішно прийнято: {user_password}")

except ValueError as err:
    print(f"\nСталася помилка! {err}")


#   ЗАВДАННЯ 2
# Є словник де ключ – логін, а значення – пароль.
# Напишіть функцію, яка запитує користувача логін та пароль.
# Якщо логіна немає в словнику, або невірний пароль, то викликати ValueError.
# Написати код try … except який використовує дану функцію.


# словник користувачів: логін -> пароль
users = {"Valerii": "12345678", "Jorg": "qwerty123", "Ivan": "password"}

print(f"\nДоступні логіни (для перевірки): {users}")  # debug


def check_login():
    # запитуємо логін та пароль
    login = input("Введіть логін: ")
    password = input("Введіть пароль: ")

    # debug-вивід
    print(f"{login = }")
    print(f"{password = }")

    # перевірка: чи є логін у словнику
    if login not in users:
        # якщо логіну немає — генеруємо виняток
        raise ValueError("Невірний логін!")

    # якщо логін є — дістаємо правильний пароль із словника
    correct_password = users[login]
    print(f"Користувач {login} знайдений у системі!")  # debug

    # перевірка пароля
    if password != correct_password:
        raise ValueError("Невірний пароль!")

    # якщо все вірно — повертаємо, наприклад, логін
    return login


# блок з обробкою винятків
try:
    current_user = check_login()
    print(f"Вхід виконано успішно. Користувач: {current_user}")

except ValueError as err:
    print(f"Сталася помилка при вході: {err}")
