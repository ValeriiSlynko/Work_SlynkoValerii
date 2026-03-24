# Модуль 6. Функції
# Тема: Функції. Частина 5
# Завдання 1
# Напишіть власний модуль string_utils.py з наступними функціями:
# Видалення знаків пунктуації з рядка, а саме: ,.?!;:
# Підрахунок кількості голосних у рядку
# Перевірка чи є рядок паліндромом(читається однаково задом наперед)
# Імпортуйте цей модуль в іншому файлі та використайте всі 3 функції.
# Додатково у файлі string_utils.py напишіть код перевірки роботи функцій: користувач вводить назву функції та рядок,
# потрібно вивести результат.
# Ця перевірка не повинна запускатись при імпорті в іншому файлі.


def delete_punctuation(text: str) -> str:
    punctuation = ",.?!;:"
    for symbol in punctuation:
        text = text.replace(symbol, "")
    return text


def count_vowels(text: str) -> int:
    vowels = "aeiouyаеєиіїоуюяAEIOUYАЕЄИІЇОУЮЯ"
    count = 0
    for ch in text:
        if ch in vowels:
            count += 1
    return count


def is_palindrome(text: str) -> bool:
    cleaned = text.replace("поп ", "поп").lower()
    return cleaned == cleaned[::-1]
