def F(n):
    bin_n = bin(n)[2:]
    OneCount, ZeroCount = 0, 0
    for i in range(len(bin_n)):
        if (i + 1) % 2 == 0 and bin_n[i] == '1':
            OneCount += 1
        elif (i + 1) % 2 == 1 and bin_n[i] == '0':
            ZeroCount += 1
    print(bin_n, OneCount, ZeroCount)
    return (abs(OneCount - ZeroCount))


n = 1

while F(n) != 5:
    n += 1
print(n, F(n))
