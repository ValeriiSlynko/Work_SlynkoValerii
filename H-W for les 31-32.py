#   Завдання 1
# Фінансова звітність для різних організацій
# Щороку ваша компанія надає різним державним організаціям фінансову звітність.
# Залежно від організації формати звітності різні.
# Використовуючи механізм декораторів, вирішіть питання звітності для організацій.


def add_header(org_name: str):
    """
    Фабрика декораторів, яка створює декоратор для додавання заголовка
    з назвою державної організації.

    :param org_name: str - назва організації
    :return: декоратор, який додає заголовок до сформованого звіту
    """

    def decorator(func):
        """
        Декоратор, що приймає функцію формування звіту.
        """

        def wrapper(income: int, expenses: int, taxes: int) -> str:
            """
            Обгортка, яка викликає функцію та додає заголовок.

            :param income: int - дохід
            :param expenses: int - витрати
            :param taxes: int - податки
            :return: str - текст звіту з доданим заголовком
            """
            # TODO:
            # 1. Викликати базову функцію:
            #    base = func(income, expenses, taxes)
            #
            # 2. Додати заголовок:
            #    result = f"=== {org_name} ===\n" + base
            #
            # 3. Повернути result

            # Виклик базової функції
            base = func(income, expenses, taxes)

            # Додаємо заголовок
            result = f"===={org_name}====\n" + base
            # Повертаємо результат
            return result

        return wrapper

    return decorator


def base_report(income: int, expenses: int, taxes: int) -> str:
    """
    Базова функція формування фінансового звіту.

    :param income: int - дохід
    :param expenses: int - витрати
    :param taxes: int - податки
    :return: str - текст базового звіту
    """
    # TODO:
    # Сформувати рядок зі звітом, наприклад:
    # text = f"Дохід: {income}\nВитрати: {expenses}\nПодатки: {taxes}"
    # return text

    text = f"Дохід: {income}\nВитрати: {expenses}\nПодатки: {taxes}"
    return text


@add_header("Податкова служба України")
def tax_report(income: int, expenses: int, taxes: int) -> str:
    """
    Звіт для податкової служби.

    :return: str - текст звіту
    """
    # TODO:
    # Просто повернути результат базової функції:
    # return base_report(income, expenses, taxes)

    return base_report(income, expenses, taxes)


@add_header("Орган державної статистики")
def stats_report(income: int, expenses: int, taxes: int) -> str:
    """
    Звіт для органу статистики.

    :return: str - текст звіту
    """
    # TODO:
    # return base_report(income, expenses, taxes)

    return base_report(income, expenses, taxes)


def main() -> None:
    """
    Точка входу програми.

    Викликає функції для формування звітів.
    """
    income = 100000
    expenses = 50000
    taxes = 15000

    # TODO: розкоментувати після реалізації
    # print(tax_report(income, expenses, taxes))
    # print()
    # print(stats_report(income, expenses, taxes))
    print(tax_report(income, expenses, taxes))
    print()
    print(stats_report(income, expenses, taxes))


if __name__ == "__main__":
    main()


#   Завдання 2
# Аудит дій користувача
# У системі є функції, які виконують критичні операції (створення, видалення, зміна даних).
# Потрібно автоматично фіксувати в журналі хто виконав дію, яку саме дію, з якими параметрами та коли.
# Використовуйте декоратори, реалізуйте аудит для таких функцій.


import datetime


def audit(user_name: str):
    """
    Фабрика декораторів для аудиту дій користувача.

    Додатково обгортає функцію так, щоб:
    - перед її виконанням записати у журнал:
        хто виконав дію, яку саме дію, з якими параметрами та коли.

    :param user_name: str - ім'я або логін користувача,
                        від імені якого виконується дія
    :return: функція-декоратор
    """

    def decorator(func):
        """
        Безпосередній декоратор, який приймає функцію
        (критичну операцію) та повертає її обгорнуту версію.
        """

        def wrapper(data: str) -> None:
            """
            Обгортка для функції, яка виконує аудит.

            :param data: str - дані, з якими виконується критична операція
                        (наприклад, текст запису, ідентифікатор, опис змін тощо)
            :return: None
            """
            # TODO:
            # 1. Отримати поточний час:
            #    now = datetime.datetime.now()
            #
            # 2. Сформувати текст журналу.
            #    Наприклад:
            #    log_text = (
            #        f"Користувач: {user_name}\n"
            #        f"Операція: {func.__name__}\n"
            #        f"Параметри: {data}\n"
            #        f"Час: {now}\n"
            #        "-------------------------"
            #    )
            #
            # 3. Вивести в консоль (або записати у файл):
            #    print(log_text)
            #
            # 4. Викликати оригінальну функцію:
            #    result = func(data)
            #
            # 5. Повернути result (якщо функція щось повертає).

            # Отримуємо поточний час:
            now = datetime.datetime.now()

            # Сформуємо текст журналу.

            log_text = (
                f"Користувач: {user_name}\n"
                f"Операція: {func.__name__}\n"
                f"Параметри: {data}\n"
                f"Час: {now}\n"
                "-------------------------"
            )

            # Виводимо :
            print(log_text)

            # Викликати оригінальну функцію:
            result = func(data)

            # Повернути result (якщо функція щось повертає).
            return result

        return wrapper

    return decorator


@audit("admin_user")
def create_record(data: str) -> None:
    """
    Імітація створення запису в системі.

    :param data: str - дані, які додаються (наприклад, опис нового запису)
    :return: None
    """
    # TODO:
    # Тут має бути логіка створення запису.
    # Наприклад:
    # print(f"Створено запис: {data}")

    print(f"Створено запис: {data}")


@audit("editor_user")
def update_record(data: str) -> None:
    """
    Імітація оновлення запису в системі.

    :param data: str - дані, які змінюються
    :return: None
    """
    # TODO:
    # Тут має бути логіка оновлення запису.
    # Наприклад:
    # print(f"Оновлено запис: {data}")

    print(f"Оновлено запис: {data}")


@audit("deleter_user")
def delete_record(data: str) -> None:
    """
    Імітація видалення запису в системі.

    :param data: str - дані або ідентифікатор запису, який видаляється
    :return: None
    """
    # TODO:
    # Тут має бути логіка видалення запису.
    # Наприклад:
    # print(f"Оновлено запис: {data}")

    print(f"Оновлено запис: {data}")


def main() -> None:
    """
    Точка входу в програму.

    Демонструє роботу аудиту для різних функцій:
    - створення запису
    - оновлення запису
    - видалення запису
    """
    # Приклади даних для операцій:
    create_data: str = "Новий користувач: Іван Іванов"
    update_data: str = "Зміна email для користувача: Іван Іванов"
    delete_data: str = "Видалення користувача: Іван Іванов"

    # TODO: розкоментуйте після реалізації логіки у функціях і декораторі

    create_record(create_data)
    update_record(update_data)
    delete_record(delete_data)


if __name__ == "__main__":
    main()

#   Завдання 3
# Обмеження частоти запитів
# Ви розробляєте API, і деякі функції не можна викликати надто часто, щоб не
# перевантажувати систему. Потрібно обмежити кількість викликів однієї функції за певний проміжок
# часу для одного користувача. Використовуйте декоратори, реалізуйте -rate limit- для функцій.


import time


def rate_limit(max_calls: int, period_seconds: float, user_name: str):
    """
    Фабрика декораторів для обмеження частоти виклику функції (rate limit).

    Дозволяє викликати функцію не більше max_calls разів
    за період часу period_seconds для одного користувача.

    :param max_calls: int - максимальна кількість викликів
                        (наприклад, 3 виклики)
    :param period_seconds: float - тривалість періоду в секундах,
                            за який діє обмеження (наприклад, 10.0 секунд)
    :param user_name: str - ім'я або логін користувача, для якого діє обмеження
    :return: функція-декоратор
    """

    def decorator(func):
        """
        Декоратор, який обгортає цільову функцію та додає до неї логіку
        перевірки обмеження частоти викликів.
        """
        # Локальні змінні замикання (closure), які зберігають стан:
        calls_made: int = 0  # кількість викликів у поточному періоді
        window_start: float = 0.0  # час початку поточного періоду

        def wrapper() -> None:
            """
            Обгортка для цільової функції без параметрів.

            Перевіряє, чи можна викликати функцію:
            - якщо ліміт не перевищено — викликає func()
            - якщо ліміт перевищено — виводить попередження і не викликає func()
            """
            nonlocal calls_made, window_start

            # TODO:
            # 1. Отримати поточний час:
            #    now = time.time()

            # 2. Якщо це перший виклик (window_start == 0), то:
            #    - встановити window_start = now

            # 3. Перевірити, чи минув період:
            #    якщо now - window_start >= period_seconds:
            #        - скинути лічильник: calls_made = 0
            #        - оновити початок вікна: window_start = now

            # 4. Якщо calls_made < max_calls:
            #        - збільшити лічильник: calls_made += 1
            #        - викликати оригінальну функцію: func()
            #    Інакше:
            #        - вивести повідомлення, що ліміт вичерпано, наприклад:
            #          print(f"Користувач {user_name} перевищив ліміт викликів. "
            #                f"Доступ заблоковано на {period_seconds} секунд.")

            # 5. Функція wrapper нічого не повертає (-> None), але ти можеш
            #    змінити сигнатуру, якщо хочеш повертати результат func().

            now = time.time()

            if window_start == 0:
                window_start = now

            if now - window_start >= period_seconds:
                calls_made = 0
                window_start = now

            if calls_made < max_calls:
                calls_made += 1
                func()
            else:
                print(
                    f"Користувач {user_name} перевищив ліміт викликів. "
                    f"Доступ заблоковано на {period_seconds} секунд."
                )

        return wrapper

    return decorator


@rate_limit(max_calls=3, period_seconds=10.0, user_name="user_1")
def get_data() -> None:
    """
    Імітація функції, яка звертається до API або виконує важку операцію.

    Ця функція буде обмежена декоратором rate_limit:
    - не більше 3 викликів за 10 секунд для користувача "user_1".
    """
    # TODO:
    # Тут якась корисна дія. Для демонстрації можна просто зробити:
    # print("Отримано дані з API")

    print("Отримано дані з API")


def main() -> None:
    """
    Точка входу в програму.

    Демонструє роботу обмеження частоти викликів (rate limit)
    для функції get_data().
    """
    # TODO:
    # Спробуйте викликати get_data() кілька разів підряд у циклі
    # і подивитися, як спрацьовує обмеження.
    #
    # Наприклад:
    #
    # for i in range(5):
    #     print(f"Спроба виклику №{i + 1}")
    #     get_data()
    #     time.sleep(2)  # пауза 2 секунди між спробами
    #
    # У цьому прикладі:
    # - за 10 секунд можна зробити тільки 3 успішні виклики,
    #   решта повинні виводити повідомлення про перевищення ліміту.

    for i in range(5):
        print(f"Спроба виклику №{i + 1}")
        get_data()
        time.sleep(2)


if __name__ == "__main__":
    # Приклад запуску модуля.
    main()
