def Red(stt):
    while '18' in stt or '388' in stt or '888' in stt:
        if '18' in stt:
            stt = stt.replace('18', '8', 1)
        if '388' in stt:
            stt = stt.replace('388', '81', 1)
        if '888' in stt:
            stt = stt.replace('888', '3', 1)
    return stt

for n in range(4, 10000):
    StStr = '1' + '8' * n
    Rest = Red(StStr)
    if Rest.count('1') == 3:
        print(n)