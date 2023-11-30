def End8(n):
    if str(n)[-1] == '8' and n != 8:
        return True
    else:
        return False
def Delits(n):
    res = []
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            if End8(i):
                res.append(i)
            if End8(n // i):
                res.append(n // i)
    if len(res) != 0:
        return res
    else:
        return [0]

i = 500001
res = []
while len(res) < 5:
    Delits_n = Delits(i)
    if Delits_n[0] != 0:
        res.append([i, min(Delits_n)])
    i += 1
print(res)