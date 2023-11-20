Array = list(map(int, open("17_9786").readlines()))
Max = max([x for x in Array if (abs(x) % 100) == 25])
ListS = []
def If(a, b, c):
    Tr = 0
    if len(list(str(abs(a)))) == 4:
        Tr +=1
    if len(list(str(abs(b)))) == 4:
        Tr +=1
    if len(list(str(abs(c)))) == 4:
        Tr +=1
    return(Tr <= 2)

for i in range(len(Array)-2):
    if If(Array[i], Array[i+1], Array[i+2]):
        summ = Array[i] + Array[i + 1] + Array[i + 2]
        if summ <= Max:
            ListS.append(summ)
print(len(ListS), max(ListS), Max)