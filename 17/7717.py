Array = list(map(int, open("17_7717").readlines()))
Answer = []
def Max_El_F(n):
    figure = list(map(int, list(str(n))))
    counter = 0
    for i in figure:
        if i % 2 == 0:
            counter += 1
        else:
            counter -=1
    return(counter == 0)

def FigureBigger(n, m):
    FigureN = list(map(int, list(str(n))))
    FigureM = list(map(int, list(str(m))))
    
    for i in FigureN:
        for j in FigureM:
            if i > j:
                continue
            break

        else:
            continue
        break
    else:
        return True
    return False

Need_max_el = max(list(filter(Max_El_F, Array)))

for i in range(len(Array) - 1):
    if FigureBigger(Array[i], Array[i + 1]):
        summ = sum(Array[i:i + 2])
        if summ <= Need_max_el:
            Answer.append(summ)
print(len(Answer), max(Answer))

