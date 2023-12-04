def Redactor(stt):
    while '555' in stt or '11' in stt or '2' in stt:
        if '555' in stt:
            stt = stt.replace('555', '1', 1)
        if '11' in stt:
            stt = stt.replace('11', '25', 1)
        if '2' in stt:
            stt = stt.replace('2', '5', 1)
    return stt

for n in range(101, 1000):
    StStr = '5' * n
    FinStr = Redactor(StStr)
    if FinStr == '15':
        print(n)