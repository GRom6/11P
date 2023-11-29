Array = list(map(int, open("17_9372").readlines()))

def F3(n):
    if abs(n) > 99 and abs(n) < 1000:
        return True
    return False

El_Max_1001 = max([abs(x) for x in Array if abs(x) % 1001 == 0])
res = []
for i in range(len(Array) - 1):
    flag = F3(Array[i])
    flag += F3(Array[i + 1])
    summ = Array[i] + Array[i + 1]
    if flag and summ > El_Max_1001:
        res.append(summ)

print(len(res), min(res))
