# Курс: AI+Python
# Модуль 8. Файли. Винятки
# Тема: Файли. Частина 2
from itertools import count
from os import write

#   ЗАВДАННЯ 1
# Є текстовий файл.
# Запишіть в інший файл таку статистику:
#  Кількість символів
#  Кількість рядків
#  Кількість цифр
#  Кількість голосних літер(aeuio)

#   зчитуємо вміст файлу
with open("folder_main_h-w_19.03.26/population.txt", "r", encoding = "UTF-8") as file:
    text = file.readlines()

    # кількість символів
total_chars = 0
for line in text:
    total_chars += len(line)
print(f"Кількість символів у файлі 'population.txt.' = {total_chars}")

    # кількість рядків
total_line = len(text)
print(f"Кількість рядків у файлі 'population.txt.' = {total_line}")

    # кількість цифр
total_digits = 0
for line in text:
    for digit in line:
        if digit.isdigit():
            total_digits += 1
print(f"Кількість цифр у файлі 'population.txt.' = {total_digits}")

    # кількість голосних літер
vowels = "аеиоуіaeuio"
total_vowels = 0

for line in text:
    for vowel in line:
        if vowel.lower() in vowels:
            total_vowels += 1

print(f"Кількість голосних літер у файлі 'population.txt.' = {total_vowels}")

# записуємо статистику у файл

with open("statistic.txt", "w", encoding = "UTF-8") as file:
    file.write(f"Кількість СИМВОЛІВ у файлі 'population.txt.' = {total_chars}")
    file.write(f"\nКількість РЯДКІВ у файлі 'population.txt.' = {total_line}")
    file.write(f"\nКількість ЦИФР у файлі 'population.txt' = {total_chars}")
    file.write(f"\nКількість ГОЛОСНИХ ЛІТЕР у файлі 'population.txt' = {total_vowels}")


#   ЗАВДАННЯ 2
# Користувач вводить слово та назву файлу.
# Виведіть кількість цього слова у файлі.

word = input("\nВведіть слово: ").lower()
name_file = input("Введіть назву файлу: ") # population.txt

count_words = 0

with open(name_file, "r", encoding = "UTF-8") as file:

    for line in file:
        words = line.lower().split()
        count_words += words.count(word)

print(f"Слово '{word}' зустрічається у файлі - {count_words} разів" )


#   ЗАВДАННЯ 3
# Є текстовий файл. Видаліть з нього останній рядок.

with open("statistic.txt", "r", encoding = "UTF-8") as file:
    lines = file.readline()

lines = lines[:-1]

with open("statistic.txt", "w", encoding = "UTF-8") as file:
    file.write(lines)
