Max_Sum = 0
for n in range(4, 10000):
    stringg = '1' + '2' * n
    while "12" in stringg or "322" in stringg or "222" in stringg:
        if "12" in stringg:
            stringg = stringg.replace("12", '2', 1)
        if "322" in stringg:
            stringg = stringg.replace("322", '21', 1)
        if "22" in stringg:
            stringg = stringg.replace("222", '3', 1)

    if Max_Sum < (sum(map(int, list(stringg)))):
        Max_Sum = (sum(map(int, list(stringg))))
print(Max_Sum)