def inverse(List, index):
    if List[index] == '1':
        List[index] = '0'
    else:
        List[index] = '1'
    return List
res = []
for n in range(5, 10000):
    bin_n = list(bin(n)[2:])
    Len = len(bin_n)
    if Len % 2:
        Mid_ix = (Len - 1) // 2
        bin_n = inverse(bin_n, Mid_ix)
    else:
        Mid_ix = (Len // 2) - 1
        bin_n = inverse(bin_n, Mid_ix)
        bin_n = inverse(bin_n, Mid_ix + 1)
    bin_n = ''.join(bin_n)
    R = int(bin_n, 2)
    if R > 100 and R < n:
        res.append(n)
print(min(res))


