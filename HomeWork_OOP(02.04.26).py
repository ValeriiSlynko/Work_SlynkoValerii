# Курс: AI+Python
# Модуль 11. ООП
# Тема: ООП. Частина 3

#   ЗАВДАННЯ 1
# Створіть наступні класи:
#  CreditCardPayment – атрибути currency
#  PayPalPayment – атрибути currency
#  CryptoPayment – атрибути currency
#  Методи:
#  pay(amount) – виводить повідомлення
# o CreditCardPayment – оплата карткою {amount}{currency}
# o PayPalPayment – оплата PayPal {amount}{currency}
# o CryptoPayment – оплата криптогаманцем {amount}{currency}
# Напишіть функцію create_payment() яка запитує у
# користувача тип рахунку та потрібні атрибути і повертає об’єкт.
# Створіть декілька рахунків, добавте їх у список та для кожної викличте відповідні методи.

class CreditCardPayment:
    def __init__(self, currency):
        self.currency = currency

    def pay (self, amount):
        print(f"Оплата 'CreditCardPayment' (карткою) {amount} {self.currency}")

class PayPalPayment:
    def __init__(self, currency):
        self.currency = currency

    def pay (self, amount):
        print(f"Оплата 'Pay pall' {amount} {self.currency}")


class CryptoPayment:
    def __init__(self, currency):
        self.currency = currency

    def pay (self, amount):
        print(f"Оплата криптогаманцем {amount} {self.currency}")

def create_payment():
    payment_type = input("Введіть тип оплати ('card','paypal','crypto'): ").lower()
    currency = input("Введіть валюту: ")
    if payment_type == "card":
        return CreditCardPayment(currency)
    elif payment_type == "paypal":
        return PayPalPayment(currency)
    elif payment_type == "crypto":
        return CryptoPayment(currency)
    else:
        print("Не відомий тип оплати!")
        return None

payments = []

for _ in range(3):
    payment = create_payment()
    if payment:
        payments.append(payment)

for payment in payments:
    amount = float(input("Введіть суму: "))
    payment.pay(amount)
