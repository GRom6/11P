Array = list(map(int, open('17_7718').readlines()))
res = []
for i in range(len(Array) - 1):
    for j in range(i, len(Array)):
        summ = Array[i] + Array[j]
        flag_0 = (summ) % 18 == 0
        flag_1 = (Array[i] * Array[j]) % 18 == 0
        if flag_0 != flag_1:
           res.append(summ)
print(len(res), max(res))