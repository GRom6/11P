Array = list(map(int, open("17_9704").readlines()))


def F(a, b):
    t = 0
    if len(str(a)) == 2:
        t += 1
    if len(str(b)) == 2:
        t += 1
    return (t == 1)


ParSumm = []


def InParSumm(n):
    for i in ParSumm:
        if n <= i:
            return False
    return True


for i in range(len(Array) - 1):
    if F(Array[i], Array[i + 1]):
        ParSumm.append(Array[i] + Array[i + 1])

result = list(filter(InParSumm, Array))
print(len(result), min(result))
