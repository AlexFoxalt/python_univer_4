# Запропонуйте ввести ім'я користувача та виведіть вітальне повідомлення. Hello [ім'я].
name_inp = input("Please enter your name: ").capitalize()
print(f"Hello, {name_inp}!")
print("---")

# Запропонуйте користувачеві ввести ім'я та прізвище, після чого виведіть вітальне повідомлення. Hello [ім'я] [прізвище].
first_name_inp = input("Please enter your name: ").capitalize()
last_name_inp = input("Please enter your surname: ").capitalize()
print(f"Hello, {first_name_inp} {last_name_inp}!")
print("---")

# Напишіть код, який виводить запитання та відповідь в одному рядку коду.
print("Як звуть людей, які відрізняються від усіх?\nНеповторні)")
print("---")

# Запропонуйте ввести два числа. Складіть ці числа та виведіть результат у вигляді The total is [результат].
x_inp = int(input("Please enter number X: "))
y_inp = int(input("Please enter number Y: "))
print(f"The total is {x_inp + y_inp}")
print("---")

# Запропонуйте ввести три числа. Складіть перші два та помножте суму на третє.
x_inp = int(input("Please enter number X: "))
y_inp = int(input("Please enter number Y: "))
z_inp = int(input("Please enter number Z: "))
print(f"The answer is {(x_inp + y_inp) * z_inp}")
print("---")

# Запитайте скільки шматків піци було і скільки з'їв користувач. Виведіть, скільки залишилось.
total_inp = int(input("Enter total pizza slices number: "))
eaten_inp = int(input("Enter number of slices you ate: "))
print(f"You have {total_inp - eaten_inp} slices left.")
print("---")

# Запропонуйте ввести ім'я та вік. Збільште вік на 1.
name_inp = input("Enter your name: ").capitalize()
age_inp = int(input("Enter your age: "))
print(f"{name_inp}, next birthday you will be {age_inp + 1}")
print("---")

# Запропонуйте ввести загальну суму рахунку та кількість учасників.
bill_inp = float(input("Enter total bill amount: "))
people_inp = int(input("Enter persons count: "))
print(f"Each person should pay {bill_inp / people_inp:.2f} hrn.")
print("---")

# Запропонуйте ввести кількість днів та виведіть години, хвилини і секунди.
days_inp = int(input("Enter days number: "))
print(f"Hours: {days_inp * 24}, minutes: {days_inp * 24 * 60}, seconds: {days_inp * 24 * 60 * 60}")
print("---")

# В одному кілограмі 2.204 фунта. Переведіть кілограми в фунти.
kg_inp = float(input("Please enter weight in kilograms: "))
print(f"Converted to pounds: {kg_inp * 2.204:.3f}")
print("---")

# Запропонуйте ввести число >100, потім число <10. Виведіть, скільки разів менше вміщується в більшому.
big_inp = int(input("Enter number more than 100: "))
if big_inp <= 100:
    raise ValueError("Number must be greater than 100")

small_inp = int(input("Enter number less than 10: "))
if small_inp >= 10:
    raise ValueError("Number must be less than 10")

print(f"Number {small_inp} fits into {big_inp} exactly {big_inp // small_inp} times.")
