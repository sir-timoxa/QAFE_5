"""
Задание 2.1
Напишите программу, которая проверяет здоровье персонажа в игре.
Если оно равно или меньше нуля, выведите на экран False, в противном случае True.
"""

# health = float(input())
# if health<=0:
#     print("False")
# else:
#     print("True")

"""
Задание 2.2
Напишите программу, которая проверяет является ли введенное число четным. Если да, выведите на
экран текст “Четное”, а иначе - “Нечетное”
"""

# number = float(input())
# if number % 2 == 0:
#     print("Четное")
# else:
#     print("Нечетное")

"""
Задание 2.3
Напишите программу, которая проверяет является ли год високосным. Таковыми считаются года,
которые делятся без остатка на 4 (2004, 2008) и не являются столетиями (500, 600).
Однако, если год делится без остатка  на 400, он также считается високосным (1200, 2000)
"""

# year = int(input())
# if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#     print('Високосный')
# else:
#     print('Не високосный')


"""
Задание 2.4
Напишите программу, которая печатает введенный текст заданное количество раз. Текст
и количество повторений нужно ввести с помощью inpit()
"""

# text = str(input("Enter your text: "))
# count = int(input("Enter the number of repetitions: "))
#
# for i in range(count):
#     print(text, f"#{i + 1}")
