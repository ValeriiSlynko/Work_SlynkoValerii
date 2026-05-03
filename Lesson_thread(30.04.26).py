# Модуль 14. Паралельне, багатопотокове, мережеве програмування
# ТЕМА: Паралельне, багатопотокове, мережеве програмування. Частина 1
#
#   ЗАВДАННЯ 1
# Користувач вводить з клавіатури значення у список.
# Після чого запускаються два потоки.
# Перший потік знаходить максимум у списку.
# Другий потік знаходить мінімум у списку.
# Результати обчислень виведіть на екран.

import threading


def find_max(nums, result):
    result["max"] = max(nums)
    #print(f"Максимум у списку: {maximum}")

def find_min(nums, result):
    result["min"] = min(nums)
    #print(f"Мінімум у списку: {minimum}")

nums = list(map(int,input("Введіть набір чисел: ").split(", ")))
print(f"Ви ввели список чисел: {nums}")

result = {}

thread_max = threading.Thread(target= find_max, args=(nums,result))
thread_min = threading.Thread(target= find_min, args=(nums,result))

thread_max.start()
thread_min.start()

thread_max.join()
thread_min.join()

print(f"Результат обчислення у потоках: {result}")


#   ЗАВДАННЯ 2
# Користувач вводить з клавіатури значення у список.
# Після чого запускаються два потоки.
# Перший потік знаходить суму елементів у списку.
# Другий потік знаходить середнє арифметичне у списку.
# Результати обчислень виведіть на екран.

import threading

def find_sum(numbers, result1):
    print("Початок вирахування суми елементів!")
    result1["sum"] = sum(numbers)

def find_average(numbers, result1):
    print("Початок вирахування середньої суми елементів!")
    result1["average"] = round(sum(numbers) / len(numbers),1)

numbers = list(map(int,input("Введіть значення (числа) у список: ").split(", ")))

result1 = {}

thread_sum = threading.Thread(target=find_sum, args=(numbers , result1))
thread_average = threading.Thread(target=find_average, args=(numbers, result1))

thread_sum.start()
thread_average.start()

thread_sum.join()
thread_average.join()

print(f"Сума чисел = {result1['sum']}")
print(f"Середнє значення суми чисел = {result1['average']}")

#   ЗАВДАННЯ 3
# Користувач вводить з клавіатури шлях до файлу, що містить набір чисел.
# Після чого запускаються два потоки.
# Перший потік створює новий файл, в який запише лише парні елементи списку.
# Другий потік створює новий файл, в який запише лише непарні елементи списку.
# Кількість парних і непарних елементів виводиться на екран.

# --- НЕМАЄ РОЗУМІННЯ РІШЕННЯ ---


# Завдання 4
# Користувач вводить з клавіатури шлях до файлу та слово для пошуку.
# Після чого запускається потік для пошуку цього слова у файлі.
# Результат пошуку виведіть на екран.

import threading
import json

filename = "file_fruits.json"
word = input(f"Введіть слово для пошуку у файлі {filename}: ")

def search(word, result):
    with open("file_fruits.json", "r", encoding="utf-8") as file:
        items = json.load(file)

    counter = 0

    for item in items:
        if item == word:
            counter += 1

    result [f"Кількість слів {word} "] = counter

result = {}

thread1 = threading.Thread(target=search, args=("orang", result))
thread2 = threading.Thread(target=search, args=("apple", result))
thread3 = threading.Thread(target=search, args=("banana", result))

thread1.start()
thread2.start()
thread3.start()

thread1.join()
thread2.join()
thread3.join()

print(f" {result}")
