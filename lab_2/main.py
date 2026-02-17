# 1. Запропонуйте ввести два числа. Якщо перше число більше за друге, спочатку виведіть друге число, а потім перше. В іншому випадку виведіть спочатку перше число, а потім друге.
x = int(input("Enter number X: "))
y = int(input("Enter number Y: "))
if x > y:
    print(y, x)
else:
    print(x, y)
print("---")

# 2. Запропонуйте ввести число менше 20. Якщо введене число більше або дорівнює 20, виведіть повідомлення «Too high»; в іншому випадку виведіть повідомлення "Thank you".
num = int(input("Enter number less than 20: "))
if num >= 20:
    print("Too high")
else:
    print("Thank you")
print("---")

# 3. Запропонуйте користувачеві ввести число від 10 до 20 (включно). Якщо буде введено число з цього діапазону, ведіть повідомлення «Thank you»; в іншому випадку виведіть повідомлення "Incorrect answer".
num = int(input("Enter number from 10 to 20 (included): "))
if 10 <= num <= 20:
    print("Thank you")
else:
    print("Incorrect answer")
print("---")

# 4. Запропонуйте ввести улюблений колір. Якщо він введе "red", "RED" або "Red", виведіть повідомлення "I like red too". В іншому випадку виведіть повідомлення "I don't like [colour], I prefer red".
colour = input("Enter favorite color: ")
if colour.lower() == "red":
    print("I like red too")
else:
    print(f"I don't like {colour}, I prefer red")
print("---")

# 5. Запитайте користувача, чи дощ. Перетворіть відповідь до нижнього регістру.
# Якщо користувач відповість "yes", запитайте, чи вітряно на вулиці.
# Якщо користувач відповість "yes" і на друге запитання, виведіть повідомлення "It is too windy for an umbrella"; в іншому випадку виведіть повідомлення "Take an umbrella".
# Якщо користувач не дав позитивної відповіді на перше запитання, виведіть повідомлення "Enjoy your day".
# (text = str.lower(text) Текст перетворюється на нижній регістр. Так як Python розрізняє регістр символів, введений текст зазвичай перетворюється користувачем на нижній, щоб його було зручніше перевіряти.)
rain = input("Is it rainy outside? ").lower()
if rain == "yes":
    wind = input("Is it windy outside? ").lower()
    if wind == "yes":
        print("It is too windy for an umbrella")
    else:
        print("Take an umbrella")
else:
    print("Enjoy your day")
print("---")

# 6. Запропонуйте користувачеві ввести його вік. Якщо введене значення рівне 18 і більше, виведіть повідомлення «Ви можете голосувати»;
# якщо 17 — повідомлення «Можна навчитися водити»;
# якщо 16 —«Можна купити лотерейний квиток».
# Якщо значення менше 16, виведіть повідомлення «Можна піти на гурток».
age = int(input("Enter your age: "))
if age >= 18:
    print("Ви можете голосувати")
elif age == 17:
    print("Можна навчитися водити")
elif age == 16:
    print("Можна купити лотерейний квиток")
else:
    print("Можна піти на гурток")
print("---")

# 7. Запропонуйте користувачеві ввести число.
# Якщо воно менше 10, введіть повідомлення «Занадто низько»;
# якщо число лежить в розділі від 10 до 20 — повідомлення «Правильно».
# В інших випадках введіть повідомлення «Занадто високо».
num = int(input("Enter a number: "))
if num < 10:
    print("Занадто низько")
elif 10 <= num <= 20:
    print("Правильно")
else:
    print("Занадто високо")
print("---")

# 8. Розставте код в правильному порядку:
#    1. elif time < 17:
#    2. else:
#    3. if time < 21:
#    4. ….print("Good evening!")
#    5. time = 12
#    6. ….print("Good morning!")
#    7. ….print("Good night!")
#    8. ….print("Good afternoon!")
#    9. elif time < 21:

# Task description error
# Seems to be first row is meant to be `if time < 12` (lest then 12)
# Otherwise logic is broken and impossible to implement
# Proceeding with correct statements...

time = 12
if time < 12:
    print("Good morning!")
elif time < 17:
    print("Good afternoon!")
elif time < 21:
    print("Good evening!")
else:
    print("Good night!")
print("---")

# 9. Дано натуральне число. Визначити, чи буде це число: парним, кратним 10. Виведіть відповідне повідомлення на екран.
num = int(input("Enter a natural number: "))
if num % 2 == 0:
    print(f"{num} is even")
if num % 10 == 0:
    print(f"{num} is multiple of 10")
print("---")

# 10. Перевірте, чи число введене з клавіатури є непарним, виведіть відповідне повідомлення на екран.
num = int(input("Enter a number: "))
if num % 2 != 0:
    print(f"{num} is odd")
print("---")

# 11. Визначте, чи не введений користувачем з клавіатури рядок порожній. Результат перевірки у вигляді True або False виведіть на екран.
text = input("Enter text: ")
print(text == "")
print("---")

# 12. Написати програму, яка ділитиме введені користувачем два дійсних числа і покажіть результат на екрані, повідомляючи про помилку у разі ділення на нуль.
x = float(input("Enter number X: "))
y = float(input("Enter number Y: "))
if y == 0:
    print("Error: division by zero")
else:
    print(f"{x} / {y} = {x / y:.2f}")
print("---")

# 13. Визначити, чи є введене з клавіатури натуральне число кратним трьом. Вивести результат на екран.
num = int(input("Enter a number: "))
print(num % 3 == 0)
print("---")

# 14. Розрахувати вартість покупки з урахуванням знижки в 35%, яка надається покупцеві, якщо сума покупки перевищує 20 у.о.
# Суму покупки ввести з клавіатури.
# Вивести на екран підсумкову вартість та розмір наданої знижки.
total = float(input("Enter purchase amount: "))
if total > 20:
    discount = total * 0.35
    print(f"Final price: {total - discount:.2f}$")
    print(f"Discount: {discount:.2f}$")
else:
    print(f"Final price: {total:.2f}$")
    print("Discount: 0$")
print("---")

# 15. Введіть 3 числа. Виведіть на екран найменше.
a = int(input("Enter X: "))
b = int(input("Enter Y: "))
c = int(input("Enter Z: "))
print(f"Smallest number: {min(a, b, c)}")
