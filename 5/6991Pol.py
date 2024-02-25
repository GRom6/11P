def F(n):
    bin_n = bin(n)[2:]
    bin_n += str(bin_n.count('1') % 2)
    bin_n += str(bin_n.count('1') % 2)

    return int(bin_n, 2)

n = 0
while F(n) <= 89:
    n += 1
print(n)