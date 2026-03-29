# Курс: AI+Python
# Модуль 11. ООП
# Тема: ООП. Частина 1

#   ЗАВДАННЯ 1
# Створіть клас Cart(кошик клієнта магазину) з атрибутами client(ім’я клієнта) та items(список товарів).
# Додайте метод який додає новий товар до кошика
# Додайте метод який видаляє товар з кошика
# Додайте метод для виведення інформації про кошик

class Cart:
    def __init__(self, client, items):
        self.client = client
        self.items = items

    # метод, який додає новий товар до кошика
    def add_item(self, item):
        self.items.append(item)

    # метод який видаляє товар з кошика
    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
        else:
            print(f"Товар {item} не знайдено в кошику!")

    # метод для виведення інформації про кошик
    def show_cart(self):
        print(f"Клієнт: {self.client}")
        print("Товари в кошику:", ", ".join(self.items) if self.items else "Кошик порожній")


cart_1 = Cart("Валерій", ["Картопля", "Хлібобулочні вироби","Молочні" ])
cart_1.add_item("Фрукти")
cart_1.remove_item("Хлібобулочні вироби")
cart_1.show_cart()



#   ЗАВДАННЯ 2
# Створіть клас Phone з атрибутами number та battery_level.
# Додайте метод який зменшує заряд телефона (на скільки зменшити відсотків передається як параметр),
# якщо він опуститься нижче 20%, вивести повідомлення
# Додайте метод для виведення інформації про телефон.

class Phone:
    def __init__(self, number, battery_level):
        self.number = number
        self.battery_level = battery_level

    # Метод зменшення заряду телефона
    def use_battery(self, percent):
        self.battery_level -= percent

        if self.battery_level < 20:
            print("Заряд менше 20%! Зарядіть акумулятор!")

    # Метод для виведення інформації про телефон
    def show_info(self):
        print(f"\nНомер: {self.number}, Заряд акумулятора: {self.battery_level}%")

phone_1 = Phone("097-587-53-96", 100)

phone_1.show_info()
phone_1.use_battery(85)
phone_1.show_info()
