# ЦИКЛИ. Частина 4
# Рівень 1
# Завдання 1
# Користувач вводить висоту трикутника і символ для заповнення.
# Програма повинна вивести трикутник, вирівняний по правому краю.
# Приклад введення:
# Введіть висоту: 4.
# Введіть символ: $.
# Приклад виведення:
# $
# $$
# $$$
# $$$$

# height = int(input("Введіть висоту трикутника: "))
# symbol = input("Введіть символ: ")
# print("Трикутник вирівняний по ЛІВОМУ краю")
# i = 1
# while i <= height:
#     j = 1
#     while j <= i:
#         print(symbol, end="")
#         j += 1
#     print()
#     i += 1

# height = int(input("Введіть висоту трикутника: "))
# symbol = input("Введіть символ: ")
# print("Трикутник вирівняний по ПРАВОМУ краю!")
# row = 1
# while row <= height:
#     space = height - row
#     i = 1
#     while i <= space:
#         print(" ", end=" ")
#         i += 1
#     count = 1
#     while count <= row:
#         print(symbol, end=" ")
#         count += 1
#     print()
#     row +=1

# Завдання 2
# Користувач вводить розміри дошки (ширину і висоту) і два символи для клітинок.
# Програма повинна відобразити шахову дошку, використовуючи ці символи.

# height = int(input("Введіть висоту дошки: "))
# width = int(input("Введіть ширину дошки: "))
# symbol_1 = input("Введіть 1-й символ: ")
# symbol_2 = input("Введіть 2-й символ: ")
# i = 1
# while i <= height:
#     j = 1
#     while j <= width:
#         if (i + j) % 2 == 0:
#             print(symbol_1, end=" ")
#         else:
#             print(symbol_2, end=" ")
#         j += 1
#     i +=1
#     print()

# Рівень 2
# Завдання 3
# Програма випадковим чином загадує чотиризначне число без цифр, що повторюються.
# Користувач повинен спробувати вгадати це число, вводячи свої варіанти. Після кожного введення програма повідомляє:
# Кількість цифр, які стоять на своїх місцях (бики).
# Кількість цифр, які є в числі, але стоять не на своїх місцях (корови).
# import random
# from itertools import count
# from operator import truediv
#
# from unicodedata import numeric
#
# mystery_numbers = ""
#
# while mystery_numbers == "":
#     a = random.randint(0, 9)
#     b = random.randint(0, 9)
#     c = random.randint(0, 9)
#     d = random.randint(0, 9)
#     if a != b and a != c and a != d and b != c and b != d and c != d:
#         mystery_numbers = str(a) + str(b) + str(c) + str(d)
# while True:
#     guess = input("Введіть чотиризначне значне число: ")
#     count = 0
#     for x in guess:
#         count += 1
#     if count != 4:
#         print("Введіть тільки 4 цифри")
#         continue
#
#     bulls = 0
#     cows = 0
#     i = 0
#     for symb in mystery_numbers:
#         if guess[i] == symb:
#             bulls += 1
#         elif guess[i] in mystery_numbers:
#             cows += 1
#         i += 1
#     print("Цифри, які стоять на своїх місцях (бики): ", bulls)
#     print("Цифри, які Є але стоять НЕ на своїх місцях (корови): ", cows)
#
#     if bulls == 4:
#         print("Ви вгадали число: ", bulls)
#           brake

# Завдання 4
# Число Армстронга — це число, яке дорівнює сумі своїх цифр, піднесених до степеня, що дорівнює кількості цифр.
# Напишіть програму, яка:
# Приймає одне число від користувача.
# Перевіряє, чи є воно числом Армстронга.
# Виводить відповідний результат.
# Приклади чисел Армстронга:
# 1 = 1^1 = 1
# 9 = 9^1 = 9
# 153 =1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
# 370 = 3^3 + 7^3 +0^3 =370
# 9474 = 9^4 + 4^4 + 7^4 + 4^4 = 9474

# numeric = int(input("Введіть число: "))
# check = numeric
# count = 0               # лічильник цифр у введеному числі
# temporary = numeric
# while temporary > 0:
#     temporary = temporary // 153//10
#     count += 1
#
# total = 0
# temporary = numeric  # змінна для обробки числа
# while temporary > 0:
#     digit = temporary % 10
#     total += digit ** count
#     temporary = temporary // 10
#
# if total == check:
#     print(check, "це є числом Армстронга")
# else:
#     print(check, "це НЕ є числом Армстронга")

# Рівень 3
# Завдання 5
# Користувач вводить висоту ромба (непарне число) і символ для заповнення. Програма повинна вивести заповнений ромб.
# Приклад введення:
# Введіть висоту: 5.
# Введіть символ: #.
# Приклад виведення:
#
###
#####
###
#

height = int(input("Введіть висоту (непарне число): "))
symbol = input("Введіть символ: ")

middle = height // 2

# ВЕРХНЯ ЧАСТИНА
i = 0
while i <= middle:
    spaces = middle - i
    symbols = 2 * i + 1

    j = 0
    while j < spaces:
        print(" ", end="")
        j += 1

    j = 0
    while j < symbols:
        print(symbol, end="")
        j += 1

    print()
    i += 1

# НИЖНЯ ЧАСТИНА
i = middle - 1
while i >= 0:
    spaces = middle - i
    symbols = 2 * i + 1

    j = 0
    while j < spaces:
        print(" ", end="")
        j += 1

    j = 0
    while j < symbols:
        print(symbol, end="")
        j += 1

    print()
    i -= 1

# Завдання 6
# Користувач вводить висоту ромба (непарне число) і символ для заповнення. Програма повинна вивести порожнистий ромб.
# Приклад введення:
# Введіть висоту: 7.
# Введіть символ: #.
# Приклад виведення:
# Рисунок 1

height = int(input("Введіть висоту (непарне число): "))
symbol = input("Введіть символ: ")

middle = height // 2

# БУДУЄМО ВЕРХ
i = 0
while i <= middle:
    spaces = middle - i
    symbols = 2 * i + 1

    j = 0
    while j < spaces:
        print(" ", end="")
        j += 1

    j = 0
    while j < symbols:
        if j == 0 or j == symbols - 1:
            print(symbol, end="")
        else:
            print(" ", end="")
        j += 1

    print()
    i += 1

# БУДУЄМО НИЗ
i = middle - 1
while i >= 0:
    spaces = middle - i
    symbols = 2 * i + 1

    j = 0
    while j < spaces:
        print(" ", end="")
        j += 1

    j = 0
    while j < symbols:
        if j == 0 or j == symbols - 1:
            print(symbol, end="")
        else:
            print(" ", end="")
        j += 1

    print()
    i -= 1
