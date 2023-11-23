def convert(n):
    res = ""
    while n:
        res += str(n%9)
        n //= 9
    return res[::-1]
def F(n):
    if n.count('5') == n.count('7'):
        n += n[-1]
    else:
        a = max([[n.count(str(x)), x] for x in range(10)])
        n += str(a[1])
    return n

i = 9999
while i > 0:
    n = convert(i)
    for j in range(5):
        n = F(n)
    n = int(n, 9)
    r = hex(n)[2:]
    if "bac" in r:
        print(i, r)
        break
    else:
        i -= 1
