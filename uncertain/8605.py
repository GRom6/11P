for n in range(1, 15):
    res = bin(n)[2:]
    if n % 5 == 0:
        res += res[-3:]
    else:
        res += bin(((n % 5) * 5))[2::]
    if int(res, 2) > 256:
        print(n)
        break
