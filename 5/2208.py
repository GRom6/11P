def Witch(n):
    N = 1
    for i in list(str(n)):
        N *= int(i)
    N = bin(N)[2:] + "00"
    return int(N, 2)

for i in range(1, 10000):
    for n in range(1, 10):
        N = int(str(n) * i)
        if Witch(N) == 864:
            print(N)
            break
