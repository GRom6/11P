def Redact(strr):
    while '12' in strr or '322' in strr or '222' in strr:
        if '12' in strr:
            strr = strr.replace('12', '2', 1)
        if '322' in strr:
            strr = strr.replace('322', '21', 1)
        if '222' in strr:
            strr = strr.replace('222', '3', 1)
    return strr
res = []
for n in range(4, 1000):
    strr = '1' + '2' * n
    RefStr = Redact(strr)
    res.append(len(list(RefStr)))
print(max(res))