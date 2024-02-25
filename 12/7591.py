def Redactor(strr):
    while '25' in strr or '355' in strr or '555' in strr:
        if '25' in strr:
            strr = strr.replace('25', '3', 1)
        if '355' in strr:
            strr = strr.replace('355', '52', 1)
        if '555' in strr:
            strr = strr.replace('555', '23', 1)
    return strr

for n in range(4, 10000):
    strr = '3' + '5'* n
    strr = Redactor(strr)
    if sum(map(int, list(strr))) == 27:
        print(n)
        break
        
