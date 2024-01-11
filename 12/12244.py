def Isp(strr):
    while "555" in strr or "333" in strr:
        if "555" in strr:
            strr = strr.replace("555", '3', 1)
        else:
            strr = strr.replace("333", "5", 1)
    return strr

res = 0
StrSumm = lambda x: sum(list(map(int, list(x))))
for n in range(3, 1000):
    stt = ('3' + '5' * n)
    StrSumm = lambda x: sum(list(map(int, list(x))))
    res = max(StrSumm(Isp(stt)), res)

print(res)
