# Лабораторная работа 9
# Одномерные массивы
# Программист: Машталеров Я.О., группа 643
# Принял: асс. Соколов Е.А., доц. Дмитриева Т.А.
# Дата: 24.10.2026
# Вариант 13
# Переменные: 
# left - левая граница рандома, right - правая граница рандома, 
# a - массив 1, b - массив 2, temp - временная ячейка,
# tempA - вспомогательная для массива 1, tempB - вспомогательная для массива 2,
# amaxi - индекс макс. элемента массива 1, bmaxi - индекс макс. элемента массива 2

from random import uniform

left = 1
right = 15

a = [uniform(left, right) for _ in range(round(uniform(left, right)))]
b = [uniform(left, right) for _ in range(round(uniform(left, right)))]

print(a)
print(b)
print()

tempA = 0
amaxi = 0
for k, i in enumerate(a, 0):
    if i > tempA:
        tempA = i
        amaxi = k

tempB = 0
bmaxi = 0
for k, i in enumerate(b, 0):
    if i > tempB:
        tempB = i
        bmaxi = k

temp = a[amaxi]
a[amaxi] = b[bmaxi]
b[bmaxi] = temp

print(a)
print(b)