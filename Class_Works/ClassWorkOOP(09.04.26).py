# Курс: AI+Python
# Модуль 11. ООП
# Тема: ООП. Частина 5

print("Створення 'demo' версії гри!")
#   Завдання 1
# Створіть абстрактний клас Character, атрибути
#  name – ім’я
#  max_hp – максимальний рівень здоров’я

#  hp – нинішній рівень здоров’я
#  level – рівень персонажа(від 1 до 20)
#  intelligence – стат інтелекту
#  strength – стат сили
#  dexterity – стат спритності
#  mana – стат мани
#  defense – стат захисту
# Методи:
#  attack() – абстрактний метод
#  take_damage(damage) – отримує урон, зменшений на
# захист
#  level_up() – збільшує рівень
#  increase_stat(stat) – збільшує один з статів на 1
#  rest() – відпочинок(відновлює hp до максимального)
#  heal(heal_hp) – збільшує hp на heal_hp

from abc import ABC, abstractmethod
from enum import Enum


class Stat(Enum):
    intelligence = "intelligence"
    strength = "strength"
    dexterity = "dexterity"
    mana = "mana"
    defense = "defense"

class Character(ABC):
    def __init__(
        self, name, max_hp, level, intelligence, strength, dexterity, mana, defense ):
        self._name = name
        self._max_hp = max_hp
        self._hp = max_hp
        self._level = level
        self._intelligence = intelligence
        self._strength = strength
        self._dexterity = dexterity
        self._mana = mana
        self._defense = defense

    @abstractmethod
    def attack(self, target) -> int:
        pass

    def take_damage(self, damage):
        real_damage = damage - self._defense
        if real_damage < 0:
            real_damage = 0

        self._hp -= real_damage
        if self._hp < 0:
            self._hp = 0

        print(
            f"{self._name} отримує {real_damage} урону. HP: {self._hp}/{self._max_hp}"
        )

    def level_up(self):
        if self._level < 20:
            self._level += 1
            print(f"{self._name} підняв рівень! Тепер {self._level}.")
        else:
            print(f"{self._name} вже має максимальний рівень.")

    def increase_stat(self, stat):
        if stat == Stat.intelligence:
            self._intelligence += 1
        elif stat == Stat.strength:
            self._strength += 1
        elif stat == Stat.dexterity:
            self._dexterity += 1
        elif stat == Stat.mana:
            self._mana += 1
        elif stat == Stat.defense:
            self._defense += 1
        else:
            print("Такого стату не існує.")
            return

        print(f"{self._name} збільшив стат '{stat}' на 1.")

    def rest(self):
        self._hp = self._max_hp
        print(f"{self._name} відпочив і повністю відновив HP.")

    def heal(self, heal_hp):
        self._hp += heal_hp
        if self._hp > self._max_hp:
            self._hp = self._max_hp

        print(f"{self._name} відновив {heal_hp} HP. Тепер: {self._hp}/{self._max_hp}")


#   Завдання 2
# Практичне завдання
# Створіть дочірній клас Paladin
# Методи:
#  attack() – наносить 4*strength урону та зменшує mana на
# 5, якщо недостатньо, то наносить strength урону
#  shield() – збільшує стат defense на 4+level
#  unshield() – зменшує стат defense на 4+level
#  heal_ally(ally) – лікує союзника на 5 + 2 * level + 0.5 * mana

class Paladin(Character):

    def attack(self, target) -> int:
        if self._mana >= 5:
            self._mana -= 5
            damage = 4 * self._strength
        else:
            damage = self._strength

        print(f"{self._name} атакує і наносить {damage} урону")
        target.take_damage(damage)
        return damage

    def shield(self):
        bonus = 4 + self._level
        self._defense += bonus
        print(f"{self._name} підняв захист на {bonus}")

    def unshield(self):
        bonus = 4 + self._level
        self._defense -= bonus
        print(f"{self._name} зменшив захист на {bonus}")

    def heal_ally(self, ally: Character):
        heal_up = 5 + 2 * self._level + 0.5 * self._mana
        ally.heal(int(heal_up))


#   Завдання 3
# Створіть дочірній клас Mage
# Методи:
#  attack() – наносить 3*intelligence+4 урону та зменшує
# mana на 3, якщо недостатньо, то не наносить урону
#  fireball() – наносить 2 * intelligence +3 урону по області та
# зменшує mana на 5, якщо недостатньо, то не наносить урону
#  heal_ally(ally) – лікує союзника на 3 + level + 3 * intelligence

class Mage(Character):

    def attack(self, target) -> int:
        if self._mana >= 3:
            self._mana -= 3
            damage = 3 * self._intelligence + 4
        else:
            damage = 0

        print(f"{self._name} атакує магією на {damage}")
        target.take_damage(damage)
        return damage

    def fireball(self,enemies: list ):
        if self._mana < 5:
            print("Недостатньо мани")
            return
        self._mana -= 5
        damage = 2 * self._intelligence + 3

        print(f"{self._name} кидає 'fireball' ")

        for enemy in enemies:
            enemy.take_damage(damage)

    def heal_ally(self, ally: Character):
        heal = 3 + self._level + 3 * self._intelligence
        ally.heal(int(heal))


#   Завдання 4
# Створіть дочірній клас Warrior
# Методи:
#  attack() – наносить 4*strength+3 урону
#  power_strike(enemies) – проходить по списку ворогів:
# якщо їхній рівень менший за рівень персонажа, то знищує його повністю

class Warrior(Character):

    def attack(self, target) -> int:
        damage = 4 * self._strength + 3
        print(f"{self._name} б'є на {damage}")
        target.take_damage(damage)
        return damage

    def power_strike (self, enemies: list ):
        print(f"{self._name} використовує 'power_strike' ")

        for enemy in enemies:
            if enemy._level < self._level:
                enemy._hp = 0
                print(f"{enemy._name} ЗНИЩЕНО !")


# Завдання 5
# Створіть дочірній клас Rogue
# Методи:
#  attack() – наносить strength + level урону

class Rogue(Character):

    def attack(self, target) -> int:
        damage = self._strength + self._level
        print(f"{self._name} здійснює приховану атаку {damage}")
        target.take_damage(damage)
        return damage

paladin = Paladin("Paladin", 120, 5, 5, 10, 5, 10, 8)
mage = Mage("Mage", 80, 5, 12, 3, 6, 15, 3)
warrior = Warrior("Warrior", 150, 6, 3, 12, 5, 2, 10)
rogue = Rogue("Rogue", 90, 4, 4, 8, 12, 3, 4)

# атаки
paladin.attack(warrior)
mage.attack(paladin)
rogue.attack(mage)

# спеціальні здібності
mage.fireball([paladin, warrior, rogue])
warrior.power_strike([mage, rogue])

# лікування
paladin.heal_ally(mage)

print(mage._hp)
