# Курс: AI+Python
# Модуль 13. Пакування даних
# Тема: JSON. Частина 1

#   ЗАВДАННЯ 1
# Напишіть гру вгадати число: комп’ютер загадує число від 1 до 100.
# Користувач вводить свої відповіді на що отримує підказки більше\менше.
# Якщо число вгадане менш ніж за 5 спроб, то переміг користувач, інакше комп’ютер.
#
# Реалізуйте такий функціонал:
#  почати нову гру – користувач вводить числа до правильної відповіді
#  вивести результат – кількість перемог та програшів
#  зберегти дані – зберегти кількості перемог та програшів у файл
#  завантажити дані – завантажити кількості перемог та програшів
# Реалізуйте все функціями

import random
import json

def play_game():
    number = random.randint(1,100)
    attempts = 5

    for i in range(attempts):
        guess = int(input("Введіть число від 1 до 100: "))

        if guess == number:
            print("Вітаю! Ви вгадали число")
            return True
        elif guess > number:
            print("Загадане число 'менше'")
        else:
            print("Загадане число 'більше'")

        number_attempts = attempts - i - 1
        print(f"У вас залишилось {number_attempts} спроб")

    print(f"Ви програли! Загадане число було {number}")
    return False

# створюємо функцію показу результату
def show_stats_game(wins: int, losses: int):
    print(f"Кількість перемог: {wins}")
    print(f"Кількість поразок: {losses}")

def save_stats_game(wins: int, losses: int):
    data = {"wins": wins,
            "losses": losses,
            }

    with open("stats_game.json", "w", encoding = "utf-8") as file:
        json.dump(data, file)

    print("Статистику збережено")

def load_stats_game():
    try:
        with open("stats_game.json", "r", encoding="utf-8") as file:
            data = json.load(file)

        return data["wins"], data["losses"]

    except:
        print("Файл не знайдено. Статистика обнулена.")
        return 0, 0

# створюємо головне меню гри
def main_menu():
    wins = 0
    losses = 0

    while True:
        print("\n1 - Починаємо нову гру")
        print("2 - Показати результат")
        print("3 - Зберегти результат")
        print("4 - Завантажити результат")
        print("0 - Вийти з гри")

        choice = input("Зробіть вибір: ")

        if choice == "1":
            result = play_game()
            if result:
                wins += 1
            else:
                losses += 1
        elif choice == "2":
            show_stats_game(wins, losses)
        elif choice == "3":
            save_stats_game(wins, losses)
        elif choice == "4":
            wins, losses = load_stats_game()
        elif choice == "0":
            break

if __name__ == "__main__":
    main_menu()
