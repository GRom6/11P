def Redact(strr):
    while '52' in strr or '2222' in strr or '1122' in strr:
        if '52' in strr:
            strr = strr.replace('52', '11', 1)

        if '2222' in strr:
            strr = strr.replace('2222', '5', 1)

        if '1122' in strr:
            strr = strr.replace('1122', '25', 1)
    return strr

def Sum(strr):
    Summ = sum(map(int, list(strr)))
    return Summ

# res = []
for n in range(4, 10000):
    strr = '5' + '2' * n
    ReStr = Redact(strr)
    SumStr = Sum(ReStr)
    if SumStr == 64:
        print(n)
# print(max(res))
