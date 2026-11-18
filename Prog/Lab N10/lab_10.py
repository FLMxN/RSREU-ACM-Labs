# Программа lab_10
# Двумерные массивы данных, матрицы
# Программист: Косяков Д.А., гр.6413
# Проверил: Щенева Ю.Б.
# Дата написания: 19.10.26
# Переменные:
#   n, m - число строк и число столбцов матрицы
#   a - исходная матрица, список строк
#   i, j - номер строки и номер столбца
#   mn - минимальный элемент матрицы
#   im, jm - номер строки и номер столбца минимального элемента

n = int(input())
m = int(input())

a = []
for i in range(n):
    a.append(list(map(float, input().split())))

mn = a[0][0]
im, jm = 0, 0
for i in range(n):
    for j in range(m):
        if a[i][j] < mn:
            mn = a[i][j]
            im, jm = i, j

for j in range(m):
    a[im][j] = mn
for i in range(n):
    a[i][jm] = mn

print('Минимальный элемент:', mn)
for i in range(n):
    print(*a[i])
