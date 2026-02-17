# Запропонуйте ввести ім'я користувача та виведіть вітальне повідомлення. Hello [ім'я].
print(f"Hello, {input("Please enter your name: ").capitalize()}!")
print("---")

# Запропонуйте користувачеві ввести ім'я та прізвище, після чого виведіть вітальне повідомлення. Hello [ім'я] [прізвище].
print(f"Hello, {input("Please enter your name: ").capitalize()} {input("Please enter your surname: ").capitalize()}!")
print("---")

# Напишіть код, який виводить запитання: «Як звуть людей, які відрізняються від усіх?», а в наступному рядку виводить відповідь: «Неповторні)» Спробуйте обійтися одним рядком коду.
print("Як звуть людей, які відрізняються від усіх?\nНеповторні)")
print("---")

# Запропонуйте ввести два числа. Складіть ці числа та виведіть результат у вигляді The total is [результат].
print(f"The total is: {int(input("Please enter number X: ")) + int(input("Please enter number Y: "))}")
print("---")

# Запропонуйте ввести три числа. Складіть перші два числа, а потім помножте суму на третє число. Виведіть результат у вигляді The answer is [результат].
print(f"The answer is: {(int(input("Please enter number X: ")) + int(input("Please enter number Y: "))) * int(input("Please enter number Z: "))}")
print("---")

# Запитайте скільки шматків піци було у користувача і скільки шматків він з'їв. Обчисліть, скільки шматків піци в нього залишилося, та виведіть результат у формі, зручній для користувача.
print(f"Pizza's slices left: {int(input("Enter total pizza's slices number: ")) - int(input("Enter pizza's slices number you ate: "))}")
print("---")

# Запропонуйте користувачеві ввести його ім'я та вік. Збільште вік на 1 та виведіть повідомлення: [ім'я] next birthday you will be [новий вік].
print(f"{input("Enter your name: ").capitalize()} next birthday you will be {int(input("Enter your age: ")) + 1}")
print("---")

# Запропонуйте користувачеві ввести загальну суму рахунку та запросіть загальну кількість учасників обіду. Розділіть суму рахунку на кількість учасників та виведіть суму, яку має заплатити кожен учасник.
print(f"Each person should pay: {int(input("Enter total bill amount: ")) / int(input("Enter persons count: "))} hrn.")
print("---")

# Напишіть програму, яка пропонує ввести проміжок часу в днях, а потім виводить кількість годин, хвилин та секунд у цьому проміжку.
inp = int(input("Enter days number: "))
print(f"Hours: {inp * 24}, minutes: {inp * 24 * 60}, seconds: {inp * 24 * 60 * 60}")
print("---")

# В одному кілограмі 2204 фунта. Запропонуйте ввести вагу в кілограмах і переведіть його в фунти.
print(f"Converted to kilograms: {round(int(input("Please enter weight in pounds: ")) / 2204, 3)}")
print("---")

# Запропонуйте користувачеві ввести число більше 100, а потім число менше 10. Повідомте, скільки разів «менше» вміщується у «більшому», у зручному форматі.
x_inp = int(input("Enter number more then 100: "))
if not x_inp > 100:
    raise Exception("Input number less or equal to 100")
y_inp = int(input("Enter number less then 10: "))
if not y_inp < 10:
    raise Exception("Input number more or equal to 10")
print(f"Number {x_inp} contain number {y_inp} {x_inp // y_inp} times.")