Del = lambda n, m: n % m == 0

for A in range(20000, -1, -1):
    for x in range(1, 1000000):
        if not (Del(x, 263) <= Del(x, A)) and Del(x, 71):
            break
    else:
        print(A)
        break