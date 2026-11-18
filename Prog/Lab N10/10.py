# Лабораторная работа 10
# Матрицы
# Программист: Машталеров Я.О., группа 643
# Принял: асс. Соколов Е.А., доц. Дмитриева Т.А.
# Дата: 25.10.2026
# Вариант 13
# Переменные: 
# a - матрица 1, b - матрица 2, 
# n - количество строк, m - количество столбцов,
# minA - минимальный элемент матрицы 1, minB - минимальный элемент матрицы 2,
# amini - индекс столбца с минимальным элементом матрицы 1, 
# bmini - индекс столбца с минимальным элементом матрицы 2,
# i, j - счетчики циклов, temp - временная ячейка для обмена, row - строка при выводе

n, m = 2, int(input())
print("Введите матрицу A:")
a = [[int(x) for x in input().split()] for i in range(n)]

print("Введите матрицу B:")
b = [[int(x) for x in input().split()] for i in range(n)]

amini, bmini = 0, 0
minA, minB = a[0][0], b[0][0]

for i in range(n):
    for j in range(m):
        if a[i][j] < minA:
            minA, amini = a[i][j], j
        if b[i][j] < minB:
            minB, bmini = b[i][j], j

for i in range(n):
    temp = a[i][amini]
    a[i][amini] = b[i][bmini]
    b[i][bmini] = temp

print("Матрица A:")
for row in a: print(*row)
print("Матрица B:")
for row in b: print(*row)