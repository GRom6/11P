Answ = [1000, 0]
def Invert(strr, indexs):
    strr = list(strr)
    print(strr)
    for index in indexs:
        if strr[index] == '1':
            strr[index] = '0'
        else:
            strr[index] = '1'
    print(strr)
    return "".join(strr)

for n in range(64, 1000):
    bin_n = bin(n)[2:]

    if bin_n.count('1') % 2:
        bin_n = Invert(bin_n, list(range(-5, -1, 1)))
    else:
        bin_n = Invert(bin_n, list(range(-4, 0, 1)))
    R = int(bin_n, 2)

    if Answ[0] > R:
        Answ = [R, n]

print(Answ[1])