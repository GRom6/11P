Array = list(map(int, open("17_8562").readlines()))
MinEl1 = min([x for x in Array if abs(x) < 100 and abs(x) > 9 and abs(x) % 10 == 1])
res = []
for i in range(len(Array) - 1):
    summ = Array[i] + Array[i + 1]
    flag = Array[i]**2 < MinEl1**2
    flag += Array[i + 1]**2 < MinEl1**2
    if flag == 1 and summ >= 0:
        res.append(summ)
print(len(res), min(res))