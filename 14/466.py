a = 5**1 * 7**3 + 2 * 5**2 * 7**2 + 3 * 5**3 * 7**1

def convertToX(n, b):
    res = ''
    while n:
        res += str(n % b)
        n //= b
    return res[::-1]

A_in_7 = convertToX(a, 7)
A_in_5 = convertToX(a, 5)
SumFig = lambda x: sum(map(int, list(x)))
S5 = SumFig(A_in_5)
S7 = SumFig(A_in_7)

if S5 > S7:
    print(5 + S5 - S7)
else:
    print(7 + S7 - S5)