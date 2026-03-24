# Завдання 1
# Є деякий текст. Порахуйте в цьому тексті кількість речень і виведіть на екран отриманий результат.

text = input("Напишіть декілька речень: ")
count = 0  # створюємо лічильник для розділових знаків
for char in text:
    if char == "." or char == "!" or char == "?" or char == "...":
        count += 1
print("Кількість речень, які Ви ввели = ", count)

# Завдання 2
# Користувач вводить з клавіатури рядок. Перевірте чи є введений рядок паліндромом.
# Паліндром — слово або текст, що читається однаково зліва направо і справа наліво.
# Наприклад:
# Кок;
# Козак з казок;
# Радар;
# А мене нема.

text = input("Введіть якесь слово або текст: ")

processed_text = text.lower()  # створюємо змінну та переводимо в нижній регістр
processed_text = processed_text.replace(" ", "")
processed_text = processed_text.replace(",", "")
processed_text = processed_text.replace(".", "")
processed_text = processed_text.replace("?", "")
processed_text = processed_text.replace("!", "")
processed_text = processed_text.replace(";", "")
processed_text = processed_text.replace(":", "")
processed_text = processed_text.replace("-", "")

if processed_text == processed_text[::-1]:  # порівнюємо через зворотний порядок
    print("Введений рядок являється Паліндромом!")
else:
    print("Введений рядок не є Паліндромом")

# Завдання 3
# Користувач вводить рядок і два символи. Видаліть із рядка всі символи між першим входженням
# першого символу і першим входженням другого символу, включаючи самі символи.
# Виведіть результат.

text = input("Введіть рядок: ")
symbol_1 = input("Введіть 1-й символ: ")
symbol_2 = input("введіть 2-й символ: ")

start_s1 = text.find(symbol_1)  #   зріз тексту до 1-го символу
end_s2 = text.find(symbol_2, start_s1 + 1)  #   зріз тексту від 2-го символу

if start_s1 != -1 and end_s2 != -1 and start_s1 < end_s2:
    output = text[:start_s1] + text[end_s2 + 1 :]
    print("Рядок: ", output)
else:
    print("В цьому рядку не вірні символи!")
