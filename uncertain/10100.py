Array = list(map(int, open("17_10100").readlines()))
Max = max([x for x in Array if x%100 == 13])

SummArr = []

for i in range(len(Array)-2):
    flag = 0
    flag += len(str(Array[i]))   == 3
    flag += len(str(Array[i+1])) == 3
    flag += len(str(Array[i+2])) == 3
    summ = Array[i] + Array[i+1] + Array[i+2]
    if flag == 2 and summ <= Max:
        SummArr.append(summ)

print(len(SummArr), max(SummArr))
