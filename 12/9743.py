def Redact(strr):
    while '72' in strr or '522' in strr or '2222' in strr:
        if '72' in strr:
            strr = strr.replace('72', '2', 1)
        if '522' in strr:
            strr = strr.replace('522', '27', 1)
        if '2222' in strr:
            strr = strr.replace('2222', '5', 1)
    return strr

def Sum(strr):
    Summ = sum(map(int, list(strr)))
    return Summ

for n in range(4, 10000):
    stringg = '5' + '2' * n
    ReStr = Redact(stringg)
    SumStr = Sum(ReStr)
    if SumStr == 63:
        print(n)
        break
