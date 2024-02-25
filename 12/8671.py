def Redactor(strr):
    while '46' in strr or '666' in strr:
        if '46' in strr:
            strr = strr.replace('46', '5', 1)
        if '666' in strr:
            strr = strr.replace('666', '4', 1)
    return strr

for m in range(10000):
    strr = '4' + '6'* m
    strr = Redactor(strr)
    if sum(map(int, list(strr))) > 1000:
        print(m)
        break
