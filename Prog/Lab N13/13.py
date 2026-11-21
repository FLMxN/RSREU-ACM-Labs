# Лабораторная работа 13
# Множества
# Программист: Машталеров Я.О., группа 643
# Принял: асс. Соколов Е.А., доц. Дмитриева Т.А.
# Дата: 21.11.2026
# Вариант 13
# Переменные:
#   words - исходное предложение
#   ans_vowels - множество гласных, входящих не более чем в одно слово
#   latin_vowels - множество гласных латинских букв
#   word - текущее слово
#   word_array - список слов
#   i - текущий символ
#   l - очередная гласная
#   w - очередное слово
#   cnt - количество слов, содержащих гласную

words = input()
ans_vowels = set()
latin_vowels = set("aeiou")

word = ""
word_array = []
for i in words.strip():
    if i == " ":
        if word == "":
            word += i
        else:
            word_array.append(word)
            word = ""
    else:
        word += i
if word != "":
    word_array.append(word)

for l in latin_vowels:
    cnt = 0
    for w in word_array:
        if l in w:
            cnt += 1
    if cnt <= 1:
        ans_vowels.add(l)

print(*ans_vowels)

