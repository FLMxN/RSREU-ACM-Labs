# Лабораторная работа 8
# Вложенные циклы
# Программист: Машталеров Я.О., группа 643
# Принял: асс. Соколов Е.А., доц. Дмитриева Т.А.
# Дата: 24.10.2026
# Вариант 13
# Переменные: 
# x0 - точка старта, h - шаг, xn - точка финиша
# numerator - числитель дроби, denominator - знаменатель дроби
# ans - ответ, s - сумма (сигма)

from math import *

x0 = int(input("Введите точку старта: "))
h = float(input("Введите шаг: "))
xn = int(input("Введите точку финиша: "))

x = x0
s = 0

while x < xn + h/3:
    if 0.1 < x < 0.5:
        for n in range(0, 10+1):
            numerator = x
            for _ in range(n+1):
                numerator = numerator * x
            denominator = 2*n + 3
            s += numerator/denominator
        ans = s
    elif 0.5 <= x < 1:
        for n in range(1, 7+1):
            numerator = x
            for _ in range(n):
                numerator = numerator * x
            numerator += numerator * numerator
            denominator = 8*n + 1
            s += numerator/denominator
        ans = (x+1)*s/3
    else: ans = "нет"
    print(ans)
    x += h