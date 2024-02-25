def Redactor(strr):
    while '12' in strr or '233' in strr or '3333' in strr:
        if '12' in strr:
            strr = strr.replace('12', '332', 1)
        if '233' in strr:
            strr = strr.replace('233', '23', 1)
        if '3333' in strr:
            strr = strr.replace('3333', '32', 1)
    return strr

for n in range(6, 10000):
    strr = '1' + '3'* n
    strr = Redactor(strr)
    if sum(map(int, list(strr))) % 6 == 0:
        print(n)
        break
        
