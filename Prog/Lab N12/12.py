# Лабораторная работа 12
# Подпрограммы
# Программист: Машталеров Я.О., группа 643
# Принял: асс. Соколов Е.А., доц. Дмитриева Т.А.
# Дата: 16.11.2026
# Вариант 13
# Переменные: 
# rows - количество строк матрицы, columns - количество столбцов матрицы,
# matrix - матрица
# n, k - номера строк для обнуления
# i, j - индексы циклов
# elem, row - параметры циклов (как элементы)

def input_matrix(rows: int, cols: int) -> list[list]:
    """Функция ввода матрицы с клавиатуры."""
    matrix = []
    print("Введите элементы матрицы:")
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(float(input(f"Элемент [{i+1}][{j+1}]: ")))
        matrix.append(row)
    return matrix

def output_matrix(matrix: list[list]) -> None:
    """Процедура вывода матрицы на экран."""
    for row in matrix:
        for elem in row:
            print(f"{elem}", end=" ")
        # print(*row)
        print()
    print()

def relu_for_array(arr: list) -> None:
    """Процедура обнуления всех отрицательных элементов
       в одномерном массиве."""
    for i in range(len(arr)):
        if arr[i] < 0:
            arr[i] = 0


rows = int(input("Введите кол-во строк матрицы: "))
cols = int(input("Введите кол-во столбцов матрицы: "))

matrix = input_matrix(rows, cols)

print("Матрица до:")
output_matrix(matrix)

n = int(input(f"\nn: "))
k = int(input(f"\nk: "))

relu_for_array(matrix[n - 1])
relu_for_array(matrix[k - 1])

print("Матрица после:")

output_matrix(matrix)