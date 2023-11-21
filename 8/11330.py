from itertools import product
abc = list("АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ")[::-1]

#Генерю словарь для перевода из кирилической системы счисления на 33-ичкную
Dict_for_convert = {}
for i in range(len(abc)):
    symb = abc[i]
    Dict_for_convert[symb] = i  #Я отвечает за условный 0
#print(Dict_for_convert)

#Перевожу выбранное слово по этой системе счисления
res = []
for j in "ИНФОРМАТИКА":
    print(i)
    res.append(Dict_for_convert[j])
#print(res)
res = res[::-1]

answ = 0
for i in range(len(res)):
    answ += res[i] * (len(abc) ** (i))

print(answ + 1) # + 1 т.к. отсчёт начинается с 1