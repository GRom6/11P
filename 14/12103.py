def convertTo9(n):
    res = ''
    while n:
        res += str(n % 9)
        n //= 9
    return res[::-1]
a = 361 * 2349**84 - 89**192 + 1953**481 * 4843**151
print(convertTo9(a).count('5'))