# Курс: AI+Python
# Модуль 6. Функції
# Тема: Функції. Частина 6
# Завдання 1
# Напишіть lambda-функції, які:
# Підносить число до квадрата
# Отримує довжини трикутника і повертає периметр
# Отримує прізвище та ім’я і повертає рядок у форматі«Прізвище, ім’я»
# Перевіряє чи є число парним

# a) Піднесення числа до квадрата
square = lambda x: x**2

# b) Отримання довжини трикутника і повернення периметра
perimeter = lambda a, b, c: a + b + c

# c) Отримання прізвища та ім’я і повернення рядка у форматі «Прізвище, ім’я»
format_name = lambda surname, name: f"{surname}, {name}"

# d) Перевірка чи є число парним
is_even = lambda x: x % 2 == 0

print("a) Піднесення числа до квадрату ")
num = float(input("Введіть число: "))
print(f"Квадрат числа {num} дорівнює {square(num)}")

print("\n b) Периметр трикутника через отримання його довжини ")
a = float(input("Введіть сторону a: "))
b = float(input("Введіть сторону b: "))
c = float(input("Введіть сторону c: "))
print(f"Периметр трикутника зі сторонами {a}, {b}, {c} дорівнює {perimeter(a, b, c)}")

print("\n с) Отримуємо прізвище та ім'я та повертаємо рядок")
surname = input("Введіть прізвище: ")
name = input("Введіть ім'я: ")
print(f"Результат форматування: {format_name(surname, name)}")

print("\n d) Перевірка на парність числа")
number = int(input("Введіть ціле число: "))
if is_even(number):
    print(f"Число {number} є парним.")
else:
    print(f"Число {number} є НЕпарним.")

# Завдання 2
# Напишіть функцію, яка використовуючи filter:
# Отримує список чисел та повертає список з лише додатними числами
# Отримує список слів та повертає список слів, в яких більше ніж 3 літери
# Отримує список слів та літеру і повертає список тих слів, які починаються на цю літеру (регістр неважливий)


# a) Повернення списку додатних чисел
def get_positive_numbers(numbers):
    return list(filter(lambda x: x > 0, numbers))


print("a) Повернення списку додатних чисел")
numbers_input = input("Введіть числа через пробіл: ")
numbers = list(map(float, numbers_input.split()))
positive_numbers = get_positive_numbers(numbers)
print(f"Додатні числа: {positive_numbers}")


# b) Список слів, які довші за 3 літери
def get_long_words(words):
    return list(filter(lambda word: len(word) > 3, words))


print("\n b) Список слів, які довші за 3 літери")
words_input = input("Введіть слова через пробіл: ")
words = words_input.split()
long_words = get_long_words(words)
print(f"Слова довші 3 літер: {long_words}")


# c) Список слів, що починаються на задану літеру (без урахування регістру)
def get_words_by_letter(words, letter):
    return list(filter(lambda word: word.lower().startswith(letter.lower()), words))


print("\n с) Список слів, що починаються на задану літеру (без урахування регістру)")
words_input2 = input("Введіть слова через пробіл: ")
words2 = words_input2.split()
letter = input("Введіть літеру: ")
filtered_words = get_words_by_letter(words2, letter)
print(f"Слова, що починаються на '{letter}': {filtered_words}")


# Завдання 3
# Напишіть функцію, яка отримує іншу функцію та параметри.
# Поверніть час роботи функції у секундах
# Практичне завдання
import time


def measure_time(func, *args) -> float:
    start = time.time()
    func(*args)
    end = time.time()

    return end - start


def slow_function(seconds):
    time.sleep(seconds)


result = measure_time(slow_function, 2)

print(f"Час виконання: {result:.4f} секунд")

# Завдання 4
# Напишіть функції, які:
# Сортує список слів за останньою літерою
# Сортує список чисел за кількістю цифр
# Знаходить число зі списку, яке найближче до заданого(передається як параметр)
# Знаходить слово у списку з найменшою довжиною
# Сортує список чисел за кількістю цифр, якщо кількість цифр однакова, то сортує за значенням числа


# a) функція сортує список слів за останньою літерою
def sorted_by_last_letter(words):
    return sorted(words, key=lambda word: word[-1])


print("\n Функція сортує список слів за останньою літерою")
words = input("Введіть список слів (через пробіл): ").split()
print(f"Результат відсортованих слів: {sorted_by_last_letter(words)}")


# b) функція сортує список чисел за кількістю цифр
def sorted_by_digit_count(numbers):
    return sorted(numbers, key=lambda n: len(str(n)))


print("\n Функція сортує список чисел за кількістю цифр")
numbers = list(
    map(int, input("Введіть будь-який набір чисел (через пробіл): ").split())
)
print(f"Результат відсортованих чисел: {sorted_by_digit_count(numbers)}")


# c) функція знаходить число зі списку, яке найближче до заданого (передається як параметр)
def closets_number(numbers, target):
    return min(numbers, key=lambda n: abs(n - target))


print("\n Функція знаходить число зі списку, яке найближче до заданого")
numbers_2 = list(map(int, input("Введіть список чисел: ").split()))
target = int(input("Введіть число до якого шукаємо найближче зі списку: "))
print(f"Найближче число зі списку: {closets_number(numbers_2, target)}")


# d) функція знаходить слово у списку з найменшою довжиною
def shortest_words(word):
    return min(words, key=lambda word: len(word))


print("\n Функція знаходить слово у списку з найменшою довжиною")
words_2 = list(input("Введіть список слів (через пробіл) : ").split())
print(f"Слово з найменшою довжиною: {shortest_words(words_2)}")


# e) функція сортує список чисел за кількістю цифр та значенням
def sort_numbers_complex(numbers):
    numbers = sorted(numbers)  # звичайне сортування
    return sorted(numbers, key=lambda n: len(str(n)))  # сортування за кількістю чисел


print("\n Функція сортує список чисел за кількістю цифр та значенням")
numbers_3 = list(map(int, input("Введіть числа (через пробіл): ").split()))
print(f"{sort_numbers_complex(numbers_3)}")
