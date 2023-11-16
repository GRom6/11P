def F(n):
    if not n % 3:
        n //= 3
    else:
        n -= 1

    if not n % 5:
        n //=5
    else:
        n -= 1
    
    if not n % 11:
        n //= 11
    else:
        n -= 1
    
    return n

result = 0
for n in range(10000):
    if F(n) == 8:
        result += 1

print(result)

