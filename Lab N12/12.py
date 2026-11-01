#недоделано
#Вариант 13

from random import uniform

left = 1
right = 50

def countrange(p, q, array):
    """Функция подсчёта элементов 1D массива,
        лежащих на отрезке [p; q]"""
    n = 0
    for i in array:
        if p <= i <= q: n += 1
    print(n)

n = int(input())
a = [[round(uniform(left, right)) for _ in range(n)] for _ in range(n)]
for i in a: print(*i)
print()

p = int(input("P: "))
q = int(input("Q: "))

for j in [[m[k] for m in a] for k in range(len(a))]: countrange(p, q, j)

