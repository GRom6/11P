abc = list('АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ')[::-1]
dict_n = {}

for i in range(len(abc)):
    dict_n[abc[i]] = i

numb = 0
word = list("ИНФОРМАТИКА")
for i in range(len(word)):
    numb += dict_n[word[i]] * len(abc)**(len(word) - i - 1)
print(numb + 1)