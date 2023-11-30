from functools import lru_cache
@lru_cache
def prod(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    else:
        return True
def Delits(n):
    res = []
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            if prod(i):
                res.append(i)
            if prod(n // i):
                res.append(n // i)
    if len(res) != 0:
        return res
    else:
        return [0]

i = 450001
res = []
while len(res) < 4:
    All_Delit = Delits(i)
    M = max(All_Delit) - min(All_Delit)
    if M % 29 == 11:
        res.append([i, M])
    i += 1
print(res)
