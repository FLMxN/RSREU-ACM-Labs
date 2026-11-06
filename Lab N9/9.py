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

a = [float(input()) for _ in range(int(input("Число элементов А: ")))]
b = [float(input()) for _ in range(int(input("Число элементов В: ")))]

# print(*a)
# print(*b)
# print()

tempA = -float('inf')
tempB = -float('inf')

amaxi = 0
bmaxi = 0

for i in range(len(a)):
    if a[i] > tempA:
        tempA = a[i]
        amaxi = i

for i in range(len(b)):
    if b[i] > tempB:
        tempB = b[i]
        bmaxi = i

temp = a[amaxi]
a[amaxi] = b[bmaxi]
b[bmaxi] = temp

print(*a)
print(*b)