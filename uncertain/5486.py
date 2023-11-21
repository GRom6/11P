def F(N, c):
    Bin_N = bin(N)[2:]
    if not sum(list(map(int, list(str(N))))) % 2:
        Bin_N += '0'
    else:
        Bin_N +='1'

    if c < 3:
        return F(int(Bin_N, 2), c+1)
    else:
        return int(Bin_N, 2)

Answer=[F(N, 1) for N in range(1, 1000) if F(N, 1) > 2054]
print(min(Answer))