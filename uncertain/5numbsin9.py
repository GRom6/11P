Chet = "02468"
NChet = "357" #Только одна еденица

res = 0
for i in range(5):
    number = [0,0,0,0,0]
    number[i] = 1
    if i - 1 >= 0:
        number[i - 1] = len(NChet)
    if i + 1 <= 4:
        number[i + 1] = len(NChet)

    for j in range(len(number)):
        if number[j] == 0 and j == 0:
            number[j] = len(Chet) - 1 + len(NChet)
        if number[j] == 0:
            number[j] = len(Chet) + len(NChet)
    prod = 1
    for j in number:
        prod *= j
    print(number)
    res += prod
print(res)
