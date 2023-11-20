def d(n):
    result = set()
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            if str(i)[0] == "4":
                result.add(i)
            if str(n // i)[0] == "4":
                result.add(n // i)
    if result:
        return sorted(result)
    return []

for N in range(10 ** 6):
    divisor = d(N)
    if len(divisor) == 24:
        print(N, max(divisor))

