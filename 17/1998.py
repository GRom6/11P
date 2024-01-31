List = [int(x) for x in open("17_1998.txt")]
Answ = []

def ProdOfList(List):
    Un = 1
    for Num in List:
        Un *= Num
    return  Un

for i in range(len(List) - 2):
    if abs(ProdOfList(List[i : i + 3])) % 7 == 0:
        Sum = sum(List[i : i + 3])
        if str(Sum)[-1] == '5':
            Answ.append(Sum)
print(len(Answ), max(Answ))