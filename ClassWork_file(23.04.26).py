# Курс: AI+Python
# Модуль 13. Пакування даних
# Тема: JSON. Частина 1

#   ЗАВДАННЯ 1
# Є словник з логінами(ключ) та паролями(значення) користувачів.
# Реалізуйте програму яка дозволяє:
#  завантажити дані з файлу
#  зберегти дані у файл
#  додати нового користувача
#  видалити користувача
#  зміна пароля
#  вхід у систему (якщо логін і пароль правильні)
# Реалізуйте все через функції.

import json
from typing import Any


def load_data(filename: str = "password.json") -> dict[str, str]:
    with open(filename, "r", encoding = "utf-8") as file:
        data = json.load(file)
        return data

def  save_data(data: dict [str, str] , filename: str = "password.json", ) -> None:
    with open(filename, "w", encoding = "utf-8") as file:
        json.dump(data, file, indent = 4, ensure_ascii = False)

# додати нового користувача
def add_user(data: dict[str, str]) -> None:
    login = input("Введіть логін: ")

    if login in data:
        print("Користувач існує!")
        return

    password = input("Введіть пароль: ")
    data[login] = password
    print("Користувача додано")

def delete_user(data: dict[str, str]) -> None:
    login = input("Введіть логін: ")

    if login not in data:
        print("Користувач відсутній!")
        return

    del data[login]
    print("Користувача видалено")

def change_password(data: dict[str, str]):
    login = input("Введіть логін: ")

    if login not in data:
        print("Користувач відсутній!")
        return

    new_password = input("Введіть новий пароль: ")
    data[login] = new_password
    print("Пароль змінено!")

def login_user(data: dict[str, str]):
    login = input("Введіть логін: ")
    password = input("Введіть пароль: ")

    if login in data and data[login] == password:
        print("Доступ надано!")
    else:
        print("Невірний логін або пароль")


def main_menu() -> None:
    data = load_data()
    """
    Головне меню керування користувачами.

    Дозволяє користувачу обрати одну з дій:
    - завантаження даних
    - збереження даних
    - додавання користувача
    - видалення користувача
    - зміна пароля
    - вхід у систему
    - вихід з програми

    :return: None
    """
    # TODO: завантажити дані з файлу (load_data)
    data: dict[str, str] = {}

    while True:
        print("\n=== Головне меню ===")
        print("1. Додати користувача")
        print("2. Видалити користувача")
        print("3. Змінити пароль")
        print("4. Вхід у систему")
        print("5. Зберегти дані у файл")
        print("0. Вийти")

        choice: str = input("Оберіть дію: ")

        if choice == "1":
            add_user(data)
        elif choice == "2":
            delete_user(data)
        elif choice == "3":
            change_password(data)
        elif choice == "4":
            login_user(data)
        elif choice == "5":
            save_data(data)
        elif choice == "0":
            save_data(data)
            print("Вихід з програми.")
            break
        else:
            print("Невірний вибір! Спробуйте ще раз.")

if __name__ == "__main__":
    main_menu()


# Завдання 2
# Створіть клас Cart
# Атрибути:
#  user – ім’я користувача
#  items – список товарів
#  total – загальна ціна
# Методи:
#  add(item, price) – добавити товар у кошик
#  delete(item, price) – видалити товар з кошика
#  info() – вивести інформацію про кошик
# Практичне завдання
#  save(filename) – зберегти дані у файл(за
# замовчуванням cart.json)
#  load(filename) – завантажити дані з файла (за замовчуванням cart.json)

class Cart:

    def __init__(self, user: str):
        self._user = user

        self._total = 0
        self._items = []

    def add(self, item: str, price: int ):
        self._items.append(item)
        self._total += price

    def delete(self, item: str, price: int):
        if item not in self._items:
            print("Товара не існує!")
            return

        self._items.remove(item)
        self._total -= price
        print("Товар видалено!")

    def info(self):
        print(f"\nКористувач {self._user}! Кошик товарів на суму {self._total} ")
        print(f"Список товарів: {self._items}")

    def save(self, filename: str = "cart.json"):
        data = {
            "Користувач": self._user,
            "Список товарів": self._items,
            "Загальна ціна": self._total,
        }

        with open(filename, "w", encoding = "utf-8") as file:
            json.dump(data, file, indent = 2, ensure_ascii = False)

    def load(self, filename: str = "cart.json"):
        with open(filename, "r", encoding = "utf-8") as file:
            data = json.load(file)

        self._user = data['Користувач']
        self._items = data ['Список товарів']
        self._total = data ['Загальна ціна']

cart = Cart('Валерій')

cart.add('Хліб', 25)
cart.add('Молоко', 50)
cart.add('Ковбаса', 350)

cart.info()
cart.save()

cart.load()
cart.info()

cart.add('Ківі', 70)
cart.add("Вино 'Кіндзмараулі'", 400)

cart.delete('Ковбаса', 350)
cart.save("cart.json")



# Завдання 3
# Створіть файл settings.json з базовими налаштуваннями
# програми, наприклад графічного інтерфейсу:
#  розмір зображення – 500х600
#  колір фону – сірий
#  колір кнопок – світло-сірий
#  розміщення кнопок – [100, 50]
#  інструкція користувачу

# Напишіть код, де завантажується налаштування і створюються відповідні змінні size, background_color, …

import json
with open("settings.json", "w", encoding = "utf-8") as file:
    data = {
        "Розмір зображення": [500, 600],
        "Колір фону": "Сірий",
        "Колір кнопок": "Світло-сірий",
        "Розміщення кнопок": [100, 50],
        "Інструкція користувачу": "Обери лист, фон, налаштуй колір кнопок і 'вривайся' в дизайнерський інтерфейс"
}

    json.dump(data, file, indent=2, ensure_ascii=False)

def load_settings() -> dict[str, Any]:
    with open("settings.json", "r", encoding = "utf-8") as file:
        data = json.load(file)
        return data

def save_settings(data: dict) -> None:
    with open("settings.json", "w", encoding = "utf-8") as file:
        json.dump(data, file, indent = 2, ensure_ascii=False)

def change_color(new_color: str) -> None:
    data = load_settings()
    data["Колір фону"] = new_color
    save_settings(data)

def change_size(new_color: list[int]) -> None:
    data = load_settings()
    data["Розмір зображення"] = new_color
    save_settings(data)

def show_info() -> None:
    data = load_settings()
    new = json.dumps(data, indent = 2)
    print(json.dumps(data, indent = 2, ensure_ascii = False))


change_size([1000, 500])
change_color("Жовтий")
show_info()
