# Лабораторная работа 14
# Строки
# Программист: Машталеров Я.О., группа 643
# Принял: асс. Соколов Е.А., доц. Дмитриева Т.А.
# Дата: 21.11.2026
# Вариант 13
# Переменные:
#   text1, text2 - исходные предложения
#   words - списки слов первого и второго предложений
#   k - номер обрабатываемого предложения
#   j - текущее предложение
#   word - текущее слово
#   i - текущий символ
#   w - очередное слово первого предложения

text1 = input()
text2 = input()

words = [[], []]

for k, j in enumerate((text1, text2), 0):
    word = ""
    for i in j.strip():
        if i == " ":
            if word == "":
                word += i
            else:
                words[k].append(word)
                word = ""
        else:
            word += i
    if word != "":
        words[k].append(word)

for w in words[0]:
    if w not in words[1]:
        print(w)


