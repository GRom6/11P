def Redactor(stt):
    while '555' in stt or '11' in stt or '2' in stt:
        if '555' in stt:
            stt = stt.replace('555', '1', 1)
        if '11' in stt:
            stt = stt.replace('11', '25', 1)
        if '2' in stt:
            stt = stt.replace('2', '5', 1)
    return stt

Res = [0,0]
for n in range(108, 10000, 9):
    StStr = '5' * n
    FinStr = Redactor(StStr)
    if int(FinStr) > Res[1]:
        Res = [n, int(FinStr)]
print(Res[0])