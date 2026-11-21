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

