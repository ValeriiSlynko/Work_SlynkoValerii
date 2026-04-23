# Курс: AI+Python
# Модуль 11. ООП
# Тема: ООП. Частина 6
# Завдання 1
# Створіть абстрактний клас Robot з атрибутами:
#  name – назва робота або id
#  battery_level – рівень заряду(за замовчуванням 100%)
#  status – поточний стан (один з on, off, working)
# Методи:
#  info() – виводить інформацію
#  charge() – відновлює заряд до 100%
#  turn_on() – змінює стан на on
#  turn_off() – змінює стан на off

from abc import ABC
from enum import Enum
from uuid import uuid4

class RobotStatus (Enum):
    off = "off"
    on = "on"

class Robot(ABC):
    def __init__(self, name: str = None, battery_level: int=100, status = RobotStatus.off):
        if name is None:
            name = str(uuid4())
        self._name = name
        self._battery_level = battery_level
        self._status = status  # on / off / working

    def info(self):
        print(f"Ім'я: {self._name}")
        print(f"Заряд: {self._battery_level}%")
        print(f"Статус: {self._status}")

    def charge(self):
        self._battery_level = 100
        print("Заряд відновлено")

    def turn_on(self):
        if self._battery_level <= 0:
            print("Немає заряду")
            return
        self._status = RobotStatus.on
        print("Робот увімкнено")

    def turn_off(self):
        self._status = RobotStatus.off
        print("Робот вимкнено")

robot1 = Robot("Cassio")
robot1.info()


#   Завдання 2
# Створіть дочірній клас CleaningRobot
# Додаткові атрибути:
#  dust_capacity – ємність контейнеру для пилу(за замовчуванням 0%)
#  water_capacity – ємність контейнеру для води(за замовчуванням 100%)
#  cleaning_mode – тип прибирання(вологе або сухе)
# Методи:
#  info() – додатково виводить інформацію про робота
#  turn_on() – якщо контейнер для пилу повний або контейнер для води порожній то виводить повідомлення,
# інакше запускається turn_on() з класу Robot
#  empty_dustbin() – очищає контейнер для пилу
#  fill_water() – заповнює контейнер для води
#  swap_mode() – змінює тип прибирання на протилежний
#  clean(energy, dust, water=None) – чистить поверхню,
# якщо прибирання сухе, то просто перенести пил у контейнер(якщо місця не достатньо вивести помилку),
# якщо прибирання вологе то додатково витратити воду.
# Також зменшує рівень заряду на energy


class CleaningRobot(Robot):
    def __init__(self, name):
        super().__init__(name)
        self._dust_capacity = 0
        self._water_capacity = 100
        self._cleaning_mode = "сухе"  # сухе / вологе

    def info(self):
        super().info()
        print(f"Пил: {self._dust_capacity}%")
        print(f"Вода: {self._water_capacity}%")
        print(f"Режим: {self._cleaning_mode}")

    def turn_on(self):
        if self._dust_capacity >= 100:
            print("Контейнер пилу повний")
            return

        if self._cleaning_mode == "вологе" and self._water_capacity <= 0:
            print("Немає води для вологого прибирання")
            return

        super().turn_on()

    def empty_dustbin(self):
        self._dust_capacity = 0
        print("Контейнер очищено")

    def fill_water(self):
        self._water_capacity = 100
        print("Воду заповнено")

    def swap_mode(self):
        if self._cleaning_mode == "сухе":
            self._cleaning_mode = "вологе"
        else:
            self._cleaning_mode = "сухе"
        print(f"Режим: {self._cleaning_mode}")

    def clean(self, energy, dust, water=None):
        if self._status != RobotStatus.on:
            print("Робот вимкнений")
            return

        if self._battery_level < energy:
            print("Недостатньо заряду")
            return

        # СУХЕ
        if self._cleaning_mode == "сухе":
            if self._dust_capacity + dust > 100:
                print("Немає місця для пилу")
                return
            self._dust_capacity += dust

        # ВОЛОГЕ
        else:
            if water is None:
                print("Потрібно вказати витрату води")
                return

            if self._water_capacity < water:
                print("Недостатньо води")
                return

            if self._dust_capacity + dust > 100:
                print("Немає місця для пилу")
                return

            self._dust_capacity += dust
            self._water_capacity -= water

        self._battery_level -= energy
        self._status = "working"
        print("Прибирання завершено")

print("\n--- CleaningRobot ---")

cleaner = CleaningRobot("Cleaner-2026")

cleaner.info()
cleaner.turn_on()

cleaner.clean(10, 20)
cleaner.swap_mode()
cleaner.clean(15, 10, water=20)

cleaner.info()

#   Завдання 3
# Створіть дочірній клас SecurityRobot
# Додаткові атрибути:
#  min_speed – мінімальна швидкість руху, щоб помітити  об’єкт
#  alert_level – рівень небезпеки (low, middle, high)
#  dangerous_items – список небезпечних предметів (gun, knife, bat)
# Методи:
#  info() – додатково виводить інформацію про робота
#  turn_off() – перед виключенням змінює рівень небезпеки на low
#  add_dangerous_item(item) – додає небезпечний предмет
#  remove_dangerous_item(item) – видаляє небезпечний предмет
#  detect(speed, item) – виявляє загрозу
# o якщо швидкість занизька, то ігноруємо
# o якщо швидкість велика, то рівень небезпеки middle
# o якщо це небезпечний предмет, то рівень небезпеки high
# Рівень небезпеки не може стати нижчим

class SecurityRobot(Robot):
    def __init__(self, name, min_speed):
        super().__init__(name)
        self._min_speed = min_speed
        self._alert_level = "low"
        self._dangerous_items = ["gun", "knife", "bat"]

    def info(self):
        super().info()
        print(f"Мін. швидкість: {self._min_speed}")
        print(f"Рівень небезпеки: {self._alert_level}")
        print(f"Небезпечні предмети: {self._dangerous_items}")

    def turn_off(self):
        self._alert_level = "low"
        super().turn_off()

    def add_dangerous_item(self, item):
        if item not in self._dangerous_items:
            self._dangerous_items.append(item)
            print(f"{item} додано")

    def remove_dangerous_item(self, item):
        if item in self._dangerous_items:
            self._dangerous_items.remove(item)
            print(f"{item} видалено")

    def detect(self, speed, item):
        if speed < self._min_speed:
            print("Об'єкт проігноровано")
            return

        if item in self._dangerous_items:
            self._alert_level = "high"
        elif self._alert_level != "high":
            self._alert_level = "middle"

        print(f"Рівень небезпеки: {self._alert_level}")

print("\n--- SecurityRobot ---")

guard = SecurityRobot("Robo-Security", min_speed=5)

guard.info()
guard.turn_on()

guard.detect(3, "tablet")
guard.detect(10, "bag")
guard.detect(10, "knife")

guard.info()
guard.turn_off()

#   Завдання 4
# Створіть дочірній клас AssistantRobot
# Додаткові атрибути:
#  tasks – список завдань(за замовчуванням порожній)
#  current_task – поточне завдання(за замовчуванням None)
# Методи:
#  info() – додатково виводить інформацію про робота
#  add_task(task) – додає завдання до списку
#  change_task() – змінює поточне завдання, виводить на
# екран список завдань та просить користувача вибрати
# одне з них
#  execute_task() – виконує поточне завдання, видяляє його
# зі списку, та змінює current_task на наступне

class AssistantRobot(Robot):
    def __init__(self, name):
        super().__init__(name)
        self._tasks = []
        self._current_task = None

    def info(self):
        super().info()
        print(f"Завдання: {self._tasks}")
        print(f"Поточне: {self._current_task}")

    def add_task(self, task):
        self._tasks.append(task)
        print(f"Додано: {task}")

    def change_task(self):
        if not self._tasks:
            print("Немає завдань")
            return

        print("Список завдань:")
        for i, task in enumerate(self._tasks):
            print(f"{i}: {task}")

        try:
            index = int(input("Обери номер: "))
            if 0 <= index < len(self._tasks):
                self._current_task = self._tasks[index]
                print(f"Поточне: {self._current_task}")
        except:
            print("Помилка введення")

    def execute_task(self):
        if self._current_task is None:
            print("Немає активного завдання")
            return

        print(f"Виконується: {self._current_task}")
        self._tasks.remove(self._current_task)

        if self._tasks:
            self._current_task = self._tasks[0]
        else:
            self._current_task = None

print("\n--- AssistantRobot ---")

assistant = AssistantRobot("Robo-assistant")
assistant.info()

assistant.add_task("Принести воду")
assistant.add_task("Включити світло")

assistant.change_task()   # тут буде input
assistant.execute_task()

assistant.info()
