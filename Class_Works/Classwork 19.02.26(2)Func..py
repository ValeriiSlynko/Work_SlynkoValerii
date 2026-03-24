"""
Файл використання модуля string_utils
"""

import string_utils

text = "Hello, world!"

print("Без пунктуації:", string_utils.delete_punctuation(text))
print("Кількість голосних:", string_utils.count_vowels(text))
print("Чиє текст паліндромом:", string_utils.is_palindrome(text))
