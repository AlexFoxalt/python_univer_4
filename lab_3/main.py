# 1. Перепишіть наведений нижче фрагмент коду, щоб замість використання списку [0, 1, 2, 3, 4, 5] він викликав функцію range:
# for х in [0, 1, 2, 3, 4, 5] :
# print('Люблю цю програму!')
for _ in range(6):
    print('Люблю цю програму!')
print("---")

# 2. Що покаже наведений нижче фрагмент коду?
# for number in range(6):
# print(number)
print("0\n1\n2\n3\n4\n5")
print("---")

# 3. Що покаже наведений нижче фрагмент коду?
# for number in range(2, 6):
# print(number)
print("2\n3\n4\n5")
print("---")

# 4. Що покаже наведений нижче фрагмент коду?
# for number in range(0, 501, 100):
# print(number)
print("0\n100\n200\n300\n400\n500")
print("---")

# 5. Що покаже наведений нижче фрагмент коду?
# for number in range(10, 5, -1):
# print(number)
print("10\n9\n8\n7\n6")
print("---")

# 6. Запропонуйте ввести ім'я та число, а потім виводила ім'я задану кількість разів.
name = input("Enter your name: ")
num = int(input("Enter a number: "))
for _ in range(num):
    print(name.capitalize())
print("---")

# 7. Запросіть число та Ваше ім'я. Виведіть ім'я (по одній літері в кожному рядку) і повторіть виведення рівну введеній кількості разів.
name = input("Enter your name: ")
num = int(input("Enter a number: "))
for _ in range(num):
    for letter in name:
        print(letter)
    print()
print("---")

# 8. Запропонуйте ввести число від 1 до 12. Виведіть таблицю множення для цього числа.
num = int(input("Enter a number from 1 to 12: "))
if 1 > num or num > 12:
    print("Invalid number")
else:
    for multiplier in range(1, 11):
        print(f"{num} x {multiplier} = {num * multiplier}")
print("---")

# 9. Запропонуйте ввести число до 50. Проведіть зворотний відлік від 50 до введеного числа. Простежте, щоб введене число було включено у висновок.
num = int(input("Enter a number less than 50: "))
if num < 50:
    for i in range(50, num - 1, -1):
        print(i)
else:
    print("Number must be less than 50")
print("---")

# 10. Запропонуйте ввести ім'я та число.
# Якщо число менше 10, програма має вивести ім'я задану кількість разів;
# інакше вона виводить повідомлення «Too high» тричі.
name = input("Enter your name: ")
num = int(input("Enter a number: "))
if num < 10:
    for _ in range(num):
        print(name)
else:
    for _ in range(3):
        print("Too high")
print("---")

# 11. Надайте змінній з ім'ям total значення 0.
# Запропонуйте користувачеві ввести п'ять чисел, і після кожного введення запитуйте ті, чи хоче він включити це число до підсумовування.
# Якщо відповідь буде позитивною, додайте введене число до total.
# Якщо відповідь буде негативним, число до total не додається.
# Після введення всіх п'яти чисел, виведіть значення total.
total = 0
for _ in range(5):
    num = int(input("Enter a number: "))
    add_to_total = input(f"Add {num} to total? (y/n) ").lower() == "y"
    if add_to_total:
        total += num
print("Total:", total)
print("---")

# 12. Запитайте у користувача, в якому напрямку він хоче вести відлік (у прямому чи зворотному).
# Якщо вибрано прямий відлік, запитайте число та проведіть відлік від 1 до введеного числа.
# Якщо вибрано зворотний відлік, запитайте число менше 20, а потім проведіть зворотний відлік від 20 до заданого числа.
# Якщо введено інше, виведіть повідомлення «I don't understand».
direction = input("Enter count direction (l/r): ").lower()
if direction == "r":
    num = int(input("Enter a number: "))
    for n in range(1, num + 1):
        print(n)
elif direction == "l":
    num = int(input("Enter a number less than 20: "))
    if num < 20:
        for n in range(20, num - 1, -1):
            print(n)
    else:
        print("Number must be less than 20")
else:
    print("I don't understand")
print("---")

# 13. Запитайте у користувача, скільки людей він хоче запросити на вечірку.
# Якщо буде введено число менше 10, запитайте імена та після кожного імені виведіть рядок «[ім'я] has been invited».
# Якщо введене число більше або 10, виведіть повідомлення «Too many people».
people = int(input("Enter people number: "))
if people < 10:
    for _ in range(people):
        print(input("Enter person name to invite: ").capitalize(), "has been invited")
else:
    print("Too many people")
