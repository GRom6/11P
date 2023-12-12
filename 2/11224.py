def convertTo3(n):
    res = ''
    if n == 0:
        return '0'
    while n:
        res += str(n % 3)
        n //= 3
    return res[::-1]

res = []
for i in range(4, 100000):
    Iin3 = convertTo3(i)
    SumFigIin3 = sum(map(int, list(Iin3)))

    if SumFigIin3 % 4:
        Iin3 += convertTo3((SumFigIin3 % 4) * 3)
    else:
        Iin3 = '1' + Iin3
        Iin3 = Iin3[:-2]
    
    R = int(Iin3, 3)

    if R > 353:
        res.append(R)

print(min(res))
