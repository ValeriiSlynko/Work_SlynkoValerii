# Завдання 3
# Напишіть власний модуль date_utils.py з функцією, яка отримує дату дедлайну у форматі YYYY-MM-DD.
# Поверніть кількість днів, що залишилось до дедлайну.
# Імпортуйте цей модуль в іншому файлі та використайте функцію, дедлайн вводить користувач.
# Якщо залишилось менше одного тижня до кінця дедлайна, виведіть відповідне повідомлення.
# Див datetime.date.fromisoformat()
#  datetime.date.today()
#  datetime.timedelta.days

# main.py
from date_utils import days_until_deadline


def main():
    """
    Запитує дедлайн у користувача та виводить кількість днів до нього
    :return:
    """
    deadline_input = input("Введіть дату дедлайну (YYYY-MM-DD): ").strip()

    try:
        days_left = days_until_deadline(deadline_input)
        print(f"До дедлайну залишилось {days_left} днів.")
        if days_left < 0:
            print("Дедлайн вже пройшов!")

        elif days_left < 7:
            print("УВАГА! Залишилось менше одного тижня до дедлайну!")

    except ValueError:
        print("Не правильний формат дати! Введіть у форматі YYYY-MM-DD")


if __name__ == "__main__":
    main()
