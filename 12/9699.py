def Redact(stt):
    while '71' in stt or '72' in stt or '73' in stt:
        if '71' in stt:
            stt = stt.replace('71', '227', 1)
        if '72' in stt:
            stt = stt.replace('72', '37', 1)
        if '73' in stt:
            stt = stt.replace('73', '17', 1)
    return stt

def Summ(stt):
    return sum(map(int, list(stt)))

for n in range(1, 100):
    StStr = '7' + '1' * (n + 1) + '2' * (n + 2) + '3' * (n + 3)
    ReStr = Redact(StStr)
    if Summ(ReStr) == 9 * n:
        print(n)
