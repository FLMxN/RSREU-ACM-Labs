# Лабораторная работа 10
# Матрицы
# Программист: Машталеров Я.О., группа 643
# Принял: асс. Соколов Е.А., доц. Дмитриева Т.А.
# Дата: 25.10.2026
# Вариант 13
# Переменные: 
# left - левая граница рандома, right - правая граница рандома, 
# a - матрица 1, b - матрица 2, temp - временная ячейка, n - порядок матрицы,
# tempA - вспомогательная для матрицы 1, tempB - вспомогательная для матрицы 2,
# amini - индекс столбца с минимальным элементом матрицы 1, bmini - индекс столбца с минимальным элементом матрциы 2

from random import uniform

left = 1
right = 50
n = 2

a = [[round(uniform(left, right)) for _ in range(n)], [round(uniform(left, right)) for _ in range(n)]]
b = [[round(uniform(left, right)) for _ in range(n)], [round(uniform(left, right)) for _ in range(n)]]

for i in a: print(i)
print()
for i in b: print(i)
print("---------------------------------------------------")

tempA = (right+1, [])
for i in range(len(a)):
    for j in range(len(a)):
        if a[i][j] < tempA[0]:
            tempA = (a[i][j], [a[k][j] for k in range(len(a))])
            amini = j


tempB = (right+1, [])
for i in range(len(b)):
    for j in range(len(b)):
        if b[i][j] < tempB[0]:
            tempB = (b[i][j], [b[k][j] for k in range(len(b))])
            bmini = j

for i in range(len(a)):
    for j in range(len(a)):
        if j == amini: a[i][j] = tempB[1][i]

for i in range(len(b)):
    for j in range(len(b)):
        if j == bmini: b[i][j] = tempA[1][i]

for i in a: print(i)
print()
for i in b: print(i)
print()
