def F(n):
    bin_n = bin(n)[2:]
    if bin_n.count('1') % 2 == 0:
        bin_n += bin_n[-2:]
    else:
        TimeS = bin_n[-2:].replace('1', '2').replace('0', '1').replace('2', '0')
        bin_n += TimeS
    return int(bin_n, 2)

n = 0
while F(n) <= 154:
    n += 1
print(n)