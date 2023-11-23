def convert(n):
    res = ''
    while n:
        res += str(n % 25)
        n //= 25
    return res[::-1]

res = 0
c = convert(3 * 3125 ** 8 + 2 * 625 ** 7 - 4 * 625 ** 6  + 3 * 125 ** 5 - 2 * 25**4 - 2024)
while c:
    if int(c) % 10 == 0:
        res += 1
        c //= 10
print(c)