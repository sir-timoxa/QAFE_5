"""
4.1.Напишите функцию square, принимающую 1 аргумент — сторону квадрата, и возвращающую 3
    значения(с помощью кортежа): периметр квадрата, площадь квадрата и диагональ квадрата.
"""

# def square(x):
#     a = (x * 4, x * x, (2 * (1 / 2)) * x)
#     return print(a)
#
# square((int(input())))

"""
4.2.Напишите фукнцию, которая принимает произвольное количество именнованных аргументов и выводит
    их построчно в формате аргумент: значение.Например:
    name: John
    last_name: Smith
    age: 35
    position: web
    developer
"""

#
# def arguments(**kwargs):
#     for key, value in kwargs.items():
#         print(key + ':', value)
#
#
# arguments(name="John", last_name='Smith', age=22, position='QA automation')

"""
4.3.Используя лямбда - выражение, из списка my_list = [20, -3, 15, 2, -1, -21] создайте новый
    список, содержащий только положительные числа 
"""

# my_list = [20, -3, 15, 2, -1, -21]
#
# new_list = list(filter(lambda x: x > 0, my_list))
# print(new_list)

"""
4.4.Используя лямбда выражение, получите результат перемножения значений в предыдущем списке
"""

# from functools import reduce
#
# my_list = [20, -3, 15, 2, -1, -21]
# new_list = list(filter(lambda x: x > 0, my_list))
# summa = reduce((lambda x, y: x + y), new_list)
#
# print(summa)


"""
4.5. Создайте файл my_calc.py и пропишите в нем минимум 4 функции, выполняющие базовые арифметические вычисления.
     Примените эти функции в качестве методов в другом файле.
"""
from my_calc import *

print(arithmetic(1, 2, "add")) #3
print(arithmetic(8, 2, "subtract")) #6
print(arithmetic(5, 2, "multiply")) #10
print(arithmetic(8, 2, "divide")) #4.0