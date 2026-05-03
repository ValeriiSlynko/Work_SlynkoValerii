# Курс: AI+Python
# Модуль 11. ООП
# Тема: ООП. Частина 6


# Завдання 1
# Створіть клас Passenger з атрибутами
#  name – ім’я
#  destination – місце, куди прямує

class Passenger:
    def __init__(self, name: str, destination: str):
        self._name = name
        self._destination = destination

# Завдання 2
# Створіть клас Transport з атрибутами
#  speed – швидкість
# Методи
#  move(destination, distance) – рухається до місця призначення, виводить інформацію як довго їхали

class Transport:
    def __init__(self, speed: int):
        self._speed = speed

    def move(self, destination: str, distance: int):
        time = distance / self._speed
        print(f"Рух до місця {destination} -> проїхав(ла) за {time:.2f} год.")


# Завдання 3
# Створіть клас Bus з атрибутами
#  passengers – список пасажирів(об’єкти класу Passenger)
#  capacity – максимальна можлива кількість пасажирів
# Методи
#  board_passenger(passenger) – якщо є місце, додає пасажира
#  move(destination, distance) – висаджує всіх пасажирів, які
# хочуть вийти в даному місці(виводить їхню загальну кількість) та викликає батьківський метод move()

class Bus(Transport):
    def __init__(self, speed: int, capacity: int ):
        super().__init__(speed)
        self._capacity = capacity
        self._passengers = []

    def board_passengers(self, passenger: Passenger):
        if len(self._passengers) < self._capacity:
            self._passengers.append(passenger)
            print(f"{passenger._name} зайшов(ла) в автобус")
        else:
            print("В автобусі всі місця зайняті!")

    def move(self, destination: str, distance: int):
        """ В цьому методі ми шукаємо пасажирів, які виходять з автобуса"""
        leaving_passengers = []
        for passenger in self._passengers:
            if passenger._destination == destination:
                leaving_passengers.append(passenger)

        """Якщо такі пасажири є -> видаляємо їх зі списку"""
        for passenger in leaving_passengers:
            self._passengers.remove(passenger)

        print(f"На зупинці {destination} вийшло {len(leaving_passengers)} пасажирів")

        #виклмкаємо батьківський метод
        super().move(destination, distance)

passenger1 = Passenger("Остап", "Харків")
passenger2 = Passenger("Поліна", "Чутове")
passenger3 = Passenger("Вадим", "Полтава")
passenger4 = Passenger("Анастасія", "Бориспіль")
passenger5 = Passenger("Борис", "Київ")

bus = Bus(90, 6)

bus.board_passengers(passenger1)
bus.board_passengers(passenger2)
bus.board_passengers(passenger3)
bus.board_passengers(passenger4)
bus.board_passengers(passenger5)

bus.move("Харків", 120)
bus.move("Чутове", 180)
bus.move("Полтава", 250)
bus.move("Бориспіль", 350)
bus.move("Київ", 430)
