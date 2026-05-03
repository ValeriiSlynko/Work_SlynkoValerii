# Курс: AI+Python
# Модуль 13. Пакування даних
# Тема: Pickle. Частина 2

#   ЗАВДАННЯ 1
# Напишіть програму для збереження даних про музичні групи у вигляді словника,
# де ключ – назва групи, значення – список альбомів.
# Напишіть функціонал:
#  додати новий гурт
#  додати новий альбом
#  зберегти дані через json
#  зберегти дані через pickle
#  завантажити дані через json
#  завантажити дані через pickle

import json
import pickle
from random import choice


def add_band(bands):
    name = input("Введіть назву гурту: ")

    if name in bands:
        print("Такий гурт вже існує!")
    else:
        bands[name] = []
        print("Гурт додано!")

def add_album(bands):
    name = input("Введіть назву гурту: ")

    if name not in bands:
        print("Такий гурт не існує!")
        return

    album = input("Назва альбому: ")
    bands[name].append(album)

    print("Альбом додано!")

# КРОК-1 зберігаємо дані через 'json'
def save_json(bands, filename = "bands.json"):
    with open(filename, "w", encoding = "utf-8") as file:
        json.dump(bands, file, indent = 2, ensure_ascii = False)

# КРОК-2 завантажуємо дані через 'json'
def load_json(filename = "bands.json"):
    try:
        with open(filename, "r", encoding = "utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

# КРОК-3 зберігаємо дані через 'pickle'
def save_pickle(bands, filename = "bands.pkl"):
    with open(filename, "wb") as file:
        pickle.dump(bands, file)

# КРОК-4 завантажуємо дані через 'pickle'
def load_pickle(filename = "bands.pkl"):
    try:
        with open(filename, "rb") as file:
            return pickle.load(file)
    except FileNotFoundError:
        return {}

def menu():
    bands = {}

    while True:
        print("\n Функціонал програми. Зробіть вибір")
        print("\n1. Додати гурт")
        print("2. Додати альбом")
        print("3. Зберегти JSON")
        print("4. Завантажити JSON")
        print("5. Зберегти Pickle")
        print("6. Завантажити Pickle")
        print("0. Вихід")

        choice = input("\nЗробыть свый вибір: ")

        if choice == "1":
            add_band(bands)
        elif choice == "2":
            add_album(bands)
        elif choice == "3":
            save_json(bands)
        elif choice == "4":
            bands = load_json()
        elif choice == "5":
            save_pickle(bands)
        elif choice == "6":
            bands = load_pickle()
        elif choice == "0":
            break

if __name__ == "__main__":
    menu()
