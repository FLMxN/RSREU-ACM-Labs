#недоделано
#Вариант 13

n = int(input())
k = tuple(int(input("Введите число: ")) for _ in range(n))

#1. 
x = int(input())
marker = False
for i in k:
    for j in k:
        if i==j: continue
        if i*j==x: marker = True
print('да' if marker else 'нет') 

#2.
x = int(input())
start = -1
end = 0
for cnt, i in enumerate(k, 0):
    if i==x:
        if start < 1:
            start = cnt
        else: end = cnt
if end == 0: end = len(k)
print(k[start:end+1])

#3.
x = int(input())
slash = 0
for cnt, i in enumerate(k, 0):
    if i==x:
        slash = cnt
        break
print(k[:slash]+k[slash+1:])
