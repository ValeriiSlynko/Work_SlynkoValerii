# ОПЕРАТОРИ РОЗГАЛУЖЕНЬ
# Частина 3
# Р І В Е Н Ь 1
# ЗАВДАННЯ 1
# Написати програму, яка за вибором користувача зводить введене ним число у ступінь від нульового до сьомого включно.
from calendar import month

numeric = float(input("Введіть число: "))
grad = numeric**0
grad1 = numeric**1
grad2 = round(numeric**2, 2)
grad3 = round(numeric**3, 2)
grad4 = round(numeric**4, 2)
grad5 = round(numeric**5, 2)
grad6 = round(numeric**6, 2)
grad7 = round(numeric**7, 2)
print(
    f"Число у 0-му степені: {grad};\n\t у 1-му степені {grad1};\n\t у 2-му степені {grad2};\n\t у 3-му степені {grad3};"
    f"  \n\t у 4-му степені {grad4};\n\t у 5-му степені {grad5};\n\t у 6-му степені {grad6};\n\t у 7-му степені {grad7}"
)
# # 2-й ВАРІАНТ виконання 1-го завдання:
# # Користувач вибирає до якого степеню потрібно піднести число
print(str(input("ВИКОНАННЯ ЗАВДАННЯ 2-м СПОСОБОМ")))
num = float(input("Введіть число: "))
grade = int(input("Піднести до степеню (від 0 до 7): "))
cal_0 = round(num**grade, 2)
cal_1 = round(num**grade, 2)
cal_2 = round(num**grade, 2)
cal_3 = round(num**grade, 2)
cal_4 = round(num**grade, 2)
cal_5 = round(num**grade, 2)
cal_6 = round(num**grade, 2)
cal_7 = round(num**grade, 2)
match grade:
    case 0:
        print(f"Число {num} в 0ст.= {cal_0}")
    case 1:
        print(f"Число {num} в 1ст.= {cal_1}")
    case 2:
        print(f"Число {num} в 2ст.= {cal_2}")
    case 3:
        print(f"Число {num} в 3ст.= {cal_3}")
    case 4:
        print(f"Число {num} в 4ст.= {cal_4}")
    case 5:
        print(f"Число {num} в 5ст.= {cal_5}")
    case 6:
        print(f"Число {num} в 6ст.= {cal_6}")
    case 7:
        print(f"Число {num} в 7ст.= {cal_7}")
    case _:
        print("Виберіть степінь від 0 до 7")

# ЗАВДАННЯ 2
# Написати програму підрахунку вартості розмови для різних мобільних операторів.
# Користувач вводить вартість розмови та вибирає з якого на який оператор він телефонує. Вивести вартість на екран.

cost_speak = float(input("Введіть вартість розмови, грн: "))
first_oper = int(input("Виберіть оператора (1-Kyivstar, 2-Lifecell, 3-Vodafone): "))
to_oper = int(input("До якого оператора (1-Kyivstar, 2-Lifecell, 3-Vodafone): "))

if first_oper == to_oper:
    print("Вартість розмови, грн: ", first_oper)
elif (first_oper == 1 or first_oper == 2 or first_oper == 3) and (
    to_oper == 1 or to_oper == 2 or to_oper == 3
):
    print("Вартість розмови з іншим оператором, грн: ", cost_speak * 1.25)
else:
    print("Помилка! Не вірний оператор")

# Р І В Е Н Ь 2
# ЗАВДАННЯ 3
# Користувач вводить із клавіатури число в діапазоні від 1 до 100.
# Якщо число кратне 3 (ділиться на 3 без залишку) потрібно вивести слово Fizz.
# Якщо число кратне 5 потрібно вивести слово Buzz. Якщо число кратне 3 і 5 потрібно вивести Fizz Buzz.
# Якщо число не кратне не 3 і 5 потрібно вивести саме число.
# Якщо користувач ввів значення не в діапазоні від 1 до 100 потрібно вивести повідомлення про помилку.

number = int(input("Введіть число від 0 до 100: "))

if number < 1 or number > 100:  # спочатку перевірка діапазону
    print("Помилка! Введіть число від 1 до 100")
elif number % 3 == 0 and number % 5 == 0:  # перевірка ЧИСЛА щодо ділення на 3 і 5
    print("Fizz Buzz")
elif number % 3 == 0:  # перевірка ЧИСЛА щодо ділення на 3
    print("Fizz")
elif number % 5 == 0:  # перевірка ЧИСЛА щодо ділення на 5
    print("Buzz")
elif (
    number % 3 != 0 and number % 5 != 0
):  # вивід самого ЧИСЛА у разі не ділення на 3 і 5
    print(f"Введене число: {number} не кратне 3 або 5")

# ЗАВДАННЯ 4
# Зарплата менеджера становить 200$ + відсоток від продажів, продажі до 500$ – 3%, від 500 до 1000 – 5%, понад 1000 – 8%.
# Користувач вводить із клавіатури рівень продажів для трьох менеджерів.
# Визначити їхню зарплату, визначити найкращого менеджера, нарахувати йому премію 200$, вивести підсумки на екран.

manager_1 = float(input("Рівень продажів у Івана: "))
manager_2 = float(input("Рівень продажів у Марії: "))
manager_3 = float(input("Рівень продажів у Софії: "))

salary_manager = 200  # зарплата менеджера ($)
percent_1 = 0.03  # продажі до 500$ – 3%
percent_2 = 0.05  # від 500 до 1000 – 5%
percent_3 = 0.08  # понад 1000 – 8%
bonus = 200  # змінна - премія кращому менеджеру ($)

if manager_1 < 500:
    salary_1 = salary_manager + manager_1 * percent_1
elif 500 <= manager_1 < 1000:
    salary_1 = salary_manager + manager_1 * percent_2
else:
    salary_1 = salary_manager + manager_1 * percent_3
print(f"Зарплата менеджера Івана з %: {salary_1}")
if manager_2 < 500:
    salary_2 = salary_manager + manager_2 * percent_1
elif 500 <= manager_2 < 1000:
    salary_2 = salary_manager + manager_2 * percent_2
else:
    salary_2 = salary_manager + manager_2 * percent_3
print(f"Зарплата менеджера Марії з %: {salary_2}")
if manager_3 < 500:
    salary_3 = salary_manager + manager_3 * percent_1
elif 500 <= manager_3 < 1000:
    salary_3 = salary_manager + manager_3 * percent_2
else:
    salary_3 = salary_manager + manager_3 * percent_3
print(f"Зарплата менеджера Софії з %: {salary_3}")

if manager_1 > manager_2 and manager_1 > manager_3:
    best_manager = "Іван"
    best_sales = salary_1
elif manager_2 > manager_1 and manager_2 > manager_3:
    best_manager = "Марія"
    best_sales = salary_2
elif manager_3 > manager_1 and manager_3 > manager_2:
    best_manager = "Софія"
    best_sales = salary_3
    print(
        "Кращій менеджер: ",
        best_manager,
        "!",
        "Зарплата з премією: ",
        best_sales + bonus,
    )
else:
    manager_1 == manager_2 == manager_3
    print("Кращого менеджера не визначено. Продажі однакові")

# Р І В Е Н Ь 3

# ЗАВДАННЯ 5
# Користувач вводить суму кредиту і термін (у роках).
# Програма визначає процентну ставку і розраховує загальну суму до виплати:
# Для кредиту до 10 000$ на строк до 3 років – ставка 8%.
# Для кредиту до 10 000$ на строк понад 3 роки – ставка 10%.
# Для кредиту від 10 001$ до 50 000$ на строк до 3 років – ставка 12%.
# Для кредиту від 10 001$ до 50 000$ на строк понад 3 роки – ставка 15%.
# Для кредиту понад 50 000$ на будь-який термін – ставка 20%.
# Програма виводить підсумкову суму до виплати і щомісячний платіж.

credit = float(input("Введіть суму кредиту: "))
term = float(input("Введіть термін (роки): "))
month = term * 12

if credit <= 10000 and term <= 3:
    rate = 0.08
elif credit <= 10000 and term > 3:
    rate = 0.10
elif 10001 <= credit <= 50000 and term <= 3:
    rate = 0.12
elif 10001 <= credit <= 50000 and term > 3:
    rate = 0.15
else:
    rate = 0.20

total_payment = credit + credit * rate  # розрахунок загальної сума до виплати
monthly_payment = total_payment / month  # розрахунок щомісячного платежу

print("Процентна ставка: ", round(rate * 100), "%")
print("Загальна сума до виплати: ", total_payment, "$")
print("Щомісячний платіж: ", round(monthly_payment, 2), "$")

# ЗАВДАННЯ 6

# Ви розробляєте програму для розрахунку вартості комплексного обіду в ресторані.
# Меню складається з трьох категорій: закуска, основна страва і десерт.
# Залежно від вибору клієнта і його статусу програма повинна розрахувати підсумкову вартість з урахуванням
# можливих знижок і спеціальних пропозицій.
# Умови:
# Меню комплексного обіду.
# Закуски:
# Салат – 5$,
# Суп – 7$.
# Основні страви:
# Курка – 10$,
# Риба – 12$.
# Десерти:
# Морозиво – 3$,
# Фрукти – 4$.
# Знижки.
# Якщо клієнт замовляє всі три позиції (закуску, основну страву і десерт), надається знижка 10% на все замовлення.
# Якщо сума замовлення перевищує 20$, знижка збільшується до 15%.
# Для постійних клієнтів надається додаткова знижка 5%, яка підсумовується з іншими знижками.
# Спеціальні пропозиції.
# Якщо клієнт замовляє "Суп" і "Рибу", надається знижка 2$ на десерт.
# Якщо клієнт замовляє "Курку" і "Морозиво", до замовлення додається безплатний напій (наприклад, "Чай").
# Підсумкова вартість.
# Програма повинна коректно застосувати всі знижки та спеціальні пропозиції, а потім розрахувати підсумкову вартість замовлення.

# ЗАКУСКИ
salat = 5
soup = 7
# ОСНОВНІ СТРАВИ
chicken = 10
fish = 12
# ДЕСЕРТИ
ice_cream = 3
fruit = 4

snack = str(input("Виберіть закуску (salat , soup): "))  # вибір закуски
main_course = str(
    input("Виберіть основні страви (chicken , fish): ")
)  # вибір основних страв
dessert = str(input("Виберіть десерт із списку (ice cream , fruit): "))  # вибір десерту
client_status = str(input("Ви постійний клієнт (yes or no): "))  # статус клієнта

total_amount = 0

# Розраховуємо вартість ЗАКУСКИ
if snack == "salat":
    total_amount += salat
elif snack == "soup":
    total_amount += soup
# Розраховуємо вартість ОСНОВНИХ СТРАВ
if main_course == "chicken":
    total_amount += chicken
elif main_course == "fish":
    total_amount += fish
# Розраховуємо вартість ДЕСЕРТІВ
if dessert == "ice cream":
    total_amount += ice_cream
elif dessert == "fruit":
    total_amount += fruit
print("Сума замовлення без знижок:", total_amount, "$")

# Спеціальні пропозиції
if snack == "soup" and main_course == "fish":
    total_amount -= 2
    print("Вам надається знижка на десерт: -2$")

if main_course == "chicken" and dessert == "ice cream":
    print("До Вашого замовлення безкоштовний напій - Чай")

# ЗНИЖКИ
discount = 0

if (
    snack == "salat"
    or snack == "soup"
    and main_course == "chicken"
    or main_course == "fish"
    and dessert == "ice cream"
    or dessert == "fruit"
):
    discount = 0.10  # знижка 10% при умові замовлення 3-х позицій
if total_amount > 20:
    discount = 0.15  # знижка 15% якщо сума замовлення більше 20$
if client_status == "yes":
    discount += 0.05  # додаткова знижка 5% якщо постійний клієнт

total_order_cost = total_amount - total_amount * discount

print("Загальна знижка для клієнта: ", round(discount * 100), "%")
print("Підсумкова вартість замовлення: ", total_order_cost, "$")
