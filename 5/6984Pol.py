def F(n):
    bin_n = bin(n)[2:]
    bin_n += str(bin_n.count('1') % 2)
    bin_n += str(bin_n.count('1') % 2)

    return int(bin_n, 2)

R = 100000
for n in range(0, 70):
    if F(n) > 204 and F(n) < R:
        R = F(n)
print(R)