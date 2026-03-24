# Завдання 3
# Напишіть власний модуль date_utils.py з функцією, яка отримує дату дедлайну у форматі YYYY-MM-DD.
# Поверніть кількість днів, що залишилось до дедлайну.
# Імпортуйте цей модуль в іншому файлі та використайте функцію, дедлайн вводить користувач.
# Якщо залишилось менше одного тижня до кінця дедлайна, виведіть відповідне повідомлення.
# Див datetime.date.fromisoformat()
#  datetime.date.today()
#  datetime.timedelta.days

# Створюю модуль date_utils.py

import datetime


def days_until_deadline(deadline_str: str) -> int:
    # Опис документації щодо роботи даної функції
    """
    Обчислює кількість днів до дедлайну

    :param deadline: дата дедлайну форматі YYYY-MM-DD
    :return: повертає кількість днів до дедлайну (int)
    :raises ValueError: вводимо обробку якщо формат дати некоректний (try / except)
    """  # docstring (документація рядка)

    # Перетворюємо рядок у дату
    deadline_date = datetime.date.fromisoformat(deadline_str)

    # Поточна дата
    today = datetime.date.today()

    # Різниця часу між датами
    delta = deadline_date - today

    return delta.days  # повертає


if __name__ == "__main__":
    test_date = "2026-03-10"
    print(days_until_deadline(test_date))
