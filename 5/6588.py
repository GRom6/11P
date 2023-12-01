res = []
for n in range(1, 100):
    bin_n = list(bin(n)[2:])
    for j in range(len(bin_n)):
        if bin_n[j] == '1':
            bin_n[j] = '0'
        elif bin_n[j] == '0':
            bin_n[j] = '1'

    bin_n = ''.join(bin_n)
    #print(type(bin_n))
    bin_n = '1' + bin_n
    bin_n += str(bin_n.count('1') % 2)
    R = int(bin_n, 2)
    if R > 180:
        res.append(n)
print(min(res))
