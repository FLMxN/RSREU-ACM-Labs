# Лабораторная работа 8
# Вложенные циклы
# Программист: Машталеров Я.О., группа 643
# Принял: асс. Соколов Е.А., доц. Дмитриева Т.А.
# Дата: 24.10.2026
# Вариант 13
# Переменные: 
# x0 - точка старта, h - шаг, xn - точка финиша
# num - числитель дроби, denom - знаменатель дроби
# ans - ответ, s - сумма (сигма),
# n - индекс, x - переменная

from math import *

x0 = float(input("Введите точку старта: "))
h = float(input("Введите шаг: "))
xn = float(input("Введите точку финиша: "))

x = x0

while x < xn + h/5:
    s = 0
    if 0.1 < x < 0.5:
        for n in range(0, 10+1):
            num = 1
            for _ in range(n+1):
                num = num * x
            denom = 2*n + 3
            s += num/denom
        ans = s
    elif 0.5 <= x < 1:
        for n in range(1, 7+1):
            num = 1
            for _ in range(n):
                num = num * x
            num += num * num
            denom = 8*n + 1
            s += num/denom
        ans = (x+1)*s/3
    else: ans = "не определена"
    print(ans)
    x += h