# Курс: AI+Python
# Модуль 8. Файли. Винятки
# Тема: Файли. Частина 2
from os import replace

#    ЗАВДАННЯ 1
# Є текстовий файл. Виведіть кількість рядків та кількість символів в ньому

#   Кількість символів методом .read
with open("folder_main_h-w_19.03.26/population.txt", "r", encoding = "utf-8" ) as file:

    text = file.read()
count_chars = len(text)
print("Кількість символів у файлі 'population.txt' = ", count_chars)

#   Кількість рядків методом .read
count_lines = text.count("\n") + 1
print("Кількість рядків у файлі 'population.txt'", count_lines)

#   Кількість .readlines
with open("folder_main_h-w_19.03.26/population.txt", "r", encoding = "utf-8") as file:
    lines = file.readlines()

count_lines = len(lines)
count_chars = sum(len(line) for line in lines)

print(f"Кількість рядків {count_lines}")
print(f"Кількість символів {count_chars}")

#   ЗАВДАННЯ 2
# Користувач вводить ім’я та вік. Запишіть їх у файл.
# Назву файлу також вводить користувач (без розширення .txt)

name = input("\nВведіть ім'я: ")
age = int(input("Введіть вік: "))

file_name = input("Введіть назву файлу: ")
age_str = str(age)

with open(file_name + ".txt", "w", encoding = "utf-8") as file:

    file.write(name + "\n")
    file.write(age_str + "\n")


#   ЗАВДАННЯ 3
# Є текстовий файл. Запишіть його рядки в інший файл.

with open("statistic.txt", "r", encoding = "utf-8") as file:
    text = file.readlines()

#   даним методом "а" додаю інформацію, щоб автоматично не відбулось видалення у "population.txt"
with open("folder_main_h-w_19.03.26/population.txt", "a", encoding = "utf-8") as file:
    file.writelines(text)


#   ЗАВДАННЯ 4
# Користувач вводить літеру та назву файлу.
# Виведіть усі слова з файлу, які починаються на цю літеру.

letter = input("Введіть літеру: ").lower().strip()

name_file = input("Введіть назву файлу: ")

with open(name_file + ".txt", "r", encoding = "utf-8") as file:
    text = file.read()

words = text.lower().split()

print(f"Слова з файлу, які починаються на літеру '{letter}': " )
for word in words:
    if word.startswith(letter):
        print(word)


#   ЗАВДАННЯ 5
# Є текстовий файл. Замініть у ньому усі символи * на &, та навпаки.

with open("text.txt", "r", encoding = "utf-8" ) as file:
    text = file.read()
    text = text.replace("*","$")
    text = text.replace("&","*")
    text = text.replace("$", "&")

with open("text.txt", "w", encoding = "utf-8" ) as file:
    file.write(text)


#   ЗАВДАННЯ 6
# Напишіть функцію, яка отримує назву файлу та список чисел як параметри.
# Потрібно записати всі числа у файл, розмістивши кожне число на окремому рядку.
# Напишіть іншу функцію, яка отримує назву файл та читає з нього ці числа і повертає як список.

def write_name (filename, numbers):
    with open(filename, "w", encoding = "utf-8") as file:
        for number in numbers:
            file.write(str(number) + "\n")

def read_numbers (filename):
    numbers = []
    with open(filename, "r", encoding = "utf-8") as file:
        for line in file:
            numbers.append(int(line.strip()))

    return numbers

numbers = [10, 15, 20, 25, 30]
write_name("text.txt", numbers)

result = read_numbers("text.txt")

print(result)

#   ЗАВДАННЯ 7
# Є 2 файли, запишіть у третій файл лише ті символи, які є в обох файлах одночасно

with open("test.txt", "r", encoding = "utf-8") as file1:
    text1 = file1.read()

with open("folder_main_h-w_19.03.26/population.txt", "r", encoding = "utf-8") as file2:
    text2 = file2.read()

set1 = set(text1)
set2 = set(text2)

united = set1 & set2

with open("result.txt", "w", encoding = "utf-8") as file3:
    file3.write(" ".join(united))

#    ЗАВДАННЯ 8
# Є файл з текстом. Видаліть з нього усі неприйнятні слова.
# Список неприйнятних слів є в іншому файлі.
