def Redactor(strr):
    while '27' in strr or '377' in strr or '777' in strr:
        if '27' in strr:
            strr = strr.replace('27', '32', 1)
        if '377' in strr:
            strr = strr.replace('377', '27', 1)
        if '777' in strr:
            strr = strr.replace('777', '3', 1)
    return strr

for n in range(10, 100):
    strr = '3' + '7'* n
    strr = Redactor(strr)
    if sum(map(int, list(strr))) % 22 == 0:
        print(n)
        
