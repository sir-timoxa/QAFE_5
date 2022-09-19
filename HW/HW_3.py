"""
3.1. Дан список my_list = ['a', 'b', [1, 2, 3], 'd']. Распечатайте значения 1, 2, 3
"""
# my_list = ['a', 'b', [1, 2, 3], 'd']
# print(*my_list[2], sep=', ')

"""
3.2 Дан список list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
   - получите сумму всех чисел,
   - распечатайте все строки, где есть буква 'a'
"""
# list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
# total = 0
# words = []
# for x in list_1:
#     if type(x) == int:
#         total += x
#     if type(x) == str and 'a' in x:
#         words.append(x)
#
# print(total)
# print(*words)

"""
3.3. Превратите лист ['cat', 'dog', 'horse', 'cow'] в кортеж
"""
# words = ['cat', 'dog', 'horse', 'cow']
# words = tuple(words)
# print(type(words))

"""
3.4. Напишите программу, которая определяет, какая семья больше.
      1) Программа имеет два input() - например, family_1, family_2.
      2) Членов семьи нужно перечислить через запятую.
     Ожидаемый результат - программа выводит семью с бОльшим составом. Если состав одинаковый, print("Equal')
"""

# print("Enter first family's names separated by commas: ")
# family_1 = input().split(', ')
# print("Enter second family's names separated by commas: ")
# family_2 = input().split(', ')

# Первый вариант вывода

# if len(family_1) == len(family_2):
#     print("Equal")
# elif len(family_1) > len(family_2):
#     print("First family:", *family_1)
# else:
#     print("Second family:", *family_2)

# Второй вариант вывода
# print("Equal" if len(family_1) == len(family_2) else f"First family: {family_1}" if len(family_1) > len(
#     family_2) else f"Second family: {family_2}")

"""
3.5. Создайте словарь film c ключами title, director, year, budget, main_actor, slogan. 
    В значения можете передать информацию
    о вашем любимом фильме.
    - распечатайте только ключи
    - распечатайте только значения
    - распечатайте пары ключ - значение
"""

# film = {
#     "title": "Гаттака",
#     "director": "Эндрю Никкол",
#     "year": "1997",
#     "budget": "36000000$",
#     "main_actor": "Итан Хоук",
#     "slogan": "Каждая молекула вашего тела может предать вас"
# }
# for elem in film:
#     print(elem)
#
# for value in film.values():
#     print(value)
#
# for key, value in film.items():
#     print(key + ' : ' + value)

"""
3.6. Найдите сумму всех значений в словаре my_dictionary = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}
"""
# my_dictionary = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}
# total = 0
# for x in my_dictionary.values():
#     total += x
# print(total)

"""
3.7. Удалите повторяющиеся значения из списка [1, 2, 3, 4, 5, 3, 2, 1]
"""
# s = [1, 2, 3, 4, 5, 3, 2, 1]
# my_set=set(s)
# print(*my_set)

"""
3.8. Даны два множества: set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'}, set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}
     - найдите значения, которые встречаются в обоих множествах
     - найдите значения, которые не встречаются в обоих множествах
     - проверьте являются ли эти множества подмножествами друг друга
"""

# set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'}
# set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}
#
# print(*set1.intersection(set2))
# print(*set1.symmetric_difference(set2))
# print(set1.issubset(set2))
# print(set2.issubset(set1))