def f(n):
    bin_n = bin(n)[2:]
    if n % 2 == 0:
        bin_n += bin(sum(list(map(int, bin_n))))[2:]
    else:
        bin_n = '1' + bin_n + "00"
    return bin_n

for N in range(10000, 0, -1):
    if int(f(N), 2) < 1000:
        print(N)
        break
