# Курс: AI+Python
# Модуль 11. ООП
# Тема: ООП. Частина 2

#    ЗАВДАННЯ 1
# Напишіть клас Банківський рахунок з атрибутами:
#  ім'я клієнта
#  баланс
#  валюта
#  словник з курсом валют(однаковий для всіх)
# Додайте методи:
#  вивід загальної інформації
#  перевірка чи відома валюта(якщо ні, викликати  ValueError)
#  перевезти гроші з однієї валюти в іншу (ця операція часто використовується, тому зручно реалізувати окремим методом)
#  зміна валюти
#  поповнення балансу(валюта та сама)
#  зняття грошей з балансу(валюта та сама).

class Bank:
    # створюємо словник з курсом валют
    rates = {
        "USD": 44.5,
        "EUR": 50.2,
        "UAH": 1,}

    def __init__(self, name_client: str, balance: float, currency: dict):
        self.name_client = name_client
        self.balance = balance
        self.currency = currency

    # вивід загальної інформації
    def general_information (self):
        print(f"Ім'я клієнта банку: {self.name_client}")
        print(f"Баланс клієнта: {self.balance}")
        print(f"Курс валют: {self.currency}")

    # перевірка чи відома валюта
    def check_currency (self, currency):
        if currency not in Bank.rates:
            raise ValueError(f"Не відома валюта - {currency}")

    # конвертація валюти з однієї в іншу
    def convert (self, amount, from_currency, to_currency):
        self.check_currency(from_currency)
        self.check_currency(to_currency)

        # конверт в базову валюту
        amount_in_USD = amount / Bank.rates[from_currency]

        # перевід в цільну валюту
        return amount_in_USD * Bank.rates[to_currency]

    # заміна валюти рахунку
    def change_currency (self, new_currency: str):
        self.check_currency(new_currency)

        # конвертація балансу
        new_balance = self.convert(self.balance, self.currency, new_currency)
        self.balance = new_balance
        self.currency = new_currency

    # поповнення балансу
    def deposit (self, amount: float):
        if amount <= 0:
            raise ValueError("Сумма повинна бути більше '0' !")
        self.balance += amount

    # зняття грошей з балансу
    def withdraw (self, amount: float):
        if amount <= 0:
            raise ValueError("Сумма повинна бути більше '0' ")

        if amount > self.balance:
            raise ValueError("Недостатньо коштів на балансу!")
        self.balance -= amount

account = Bank("Valry", 5000, "UAH")

account.general_information()

account.deposit(1000)
account.withdraw(300)

account.change_currency("USD")
account.general_information()
