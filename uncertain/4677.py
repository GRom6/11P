Array = [int(i) for i in open("4677").readlines()]
Cr = len([i for i in Array if not abs(i) % 100])
res = []
for i in range(len(Array)-1):
    summ = (Array[i] + Array[i+1])

    if (Array[i] < 0 or Array[i+1] < 0) and summ < Cr:
        res.append(summ)
print(len(res), max(res))
