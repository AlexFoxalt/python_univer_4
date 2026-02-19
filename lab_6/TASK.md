1. У чому головна відмінність між списком та кортежем?

> Список это изменяемый тип данных, кортеж - нет

2. Наведіть причини існування кортежів.
> Большая эффективность по памяти и скорости обработки

3. Допустимо, що змінна my list посилається на список. Напишіть інструкцію, яка перетворює його на кортеж.
> `tuple(my_list)`

4. Припустимо, що змінна my tuple посилається на кортеж. Напишіть інструкцію, яка перетворює його на список. 
> `list(my_tuple)`

5. Якого типу даних буде результат коду? 
`a = ('s')`

> str

6. Якого типу даних буде результат коду? 
`a = 's', `

> tuple

7. Що з цього, список?
   1. ("Iron Man", "Thor", "Captain America", "Hulk")
   2. ["Iron Man", "Thor", "Captain America", "Hulk"]
   3. "Iron Man", "Thor", "Captain America", "Hulk"

> 2

8. Що з цього – правда про списки? (множинний вибір)
   1. На початку та наприкінці списку повинні стояти квадратні дужки [ ].
   2. Значення у списку поділяються комою.
   3. На початку та наприкінці списку повинні стояти круглі дужки.
   4. Значення у списку можуть мати різний формат.
   5. Значення у списку повинні мати однаковий формат

> 1. True (но не всегда, список можно создавать и функцией `list` без использования квадратных скобок)

> 2. True 

> 3. False 

> 4. True 

> 5. False

9. Створіть кортеж із назвами п'яти країн. Виведіть весь вміст кортежу. Запропонуйте користувачеві ввести назву однієї з цих країн та виведіть індекс (тобто позицію у списку) цього елемента кортежу.
```python
countries = ("UA", "GB", "PL", "CZ", "FR")
print(countries)
inp = input("Enter country code: ")
if inp in countries:
    print(countries.index(inp))
else:
    print(f"Country {inp} not found")
```

10. Допрацюйте завдання 9 так, щоб воно пропонувало користувачеві ввести число і виводило назву країни, яка знаходиться в заданій позиції.
```python
countries = ("UA", "GB", "PL", "CZ", "FR")
print(countries)
inp = int(input("Enter country index: "))
if 1 <= inp <= len(countries):
    print(countries[inp-1])
else:
    print("Position out of range")
```

11. Створіть список із назвами двох видів спорту. Запропонуйте ввести свій улюблений вид спорту і додайте його в кінець списку. Відсортуйте список та виведіть його. Поміркуйте, як це завдання виконати за допомогою кортежів.
```python
# list implementation
sports = ["football", "handball"]
sports.append(input("Enter your favorite sport: "))
print(sorted(sports))

# tuple implementation
sports = "football", "handball"
fav_sport = input("Enter your favorite sport: ")
merged_sports = sports + (fav_sport, )
print(tuple(sorted(merged_sports)))
```

12. Створіть список із назвами шести шкільних предметів. Запитайте користувача, які з цих предметів йому не подобаються. Видаліть вибрані предмети зі списку та повторно виведіть його.
```python
subjects = ["math", "history", "physics", "chemistry", "english", "vocal"]
to_delete = input("Enter comma-separated list of non-favorite subjects: ")
for subj in to_delete.split(","):
    subj = subj.strip()
    if subj in subjects:
        subjects.remove(subj)
print(subjects)
```

13. Є перелік чисел. Визначте, скільки у ньому різних чисел?
```python
from random import randint
numbers = [randint(1, 10) for i in range(10)]
print(len(set(numbers)))
```

14. Дано два списки чисел. Знайдіть однакові числа, які входять і до першого списку, і до другого. Виведіть їх у порядку зростання.
```python
from random import randint
x = [randint(1, 10) for i in range(10)]
y = [randint(1, 10) for i in range(10)]
print(sorted(set(x) & set(y)))
```
