def convertToX(n, To):
    res = []
    while n:
        res.append((n % To))
        n //= To
    return res[::-1]

res = []
for N in range(3136):
    N_in_5 = convertToX(N, 5)
    N_in_2 = convertToX(N, 2)
    N_in_16 = convertToX(N, 16)

    if len(N_in_5) <= 4 and len(N_in_2) >= 5 and N_in_16[-1] == 12:
        res.append(N)

print(len(res))