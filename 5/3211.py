for n in range(10000):
    R = bin(n)[2:]
    if n % 2 == 0:
        R += "10"
    else:
        R = '1' + R + '01'
    if int(R, 2) > 516:
        print(n)
        break