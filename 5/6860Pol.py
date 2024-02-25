def ConvertTo(number, To):
    res = []
    while number:
        res.append(number % To)
        number //= To
    if len(res) == 0:
        res.append(0)
    return res[::-1]

def ConvertFrom(number: list, From):
    res = 0
    for i in range(len(number)):
        res += number[i] * (From ** (len(number) - 1 - i))
    return res


def F(n):
    Number80 = ConvertTo(n, 80)

    SumCh = sum(filter(lambda x: x % 2 == 0, Number80))
    SumNCh = sum(filter(lambda x: x % 2, Number80))
    Number80.append(ConvertTo(max(SumCh, SumNCh), 80)[-1])

    SumCh = sum(filter(lambda x: x % 2 == 0, Number80))
    SumNCh = sum(filter(lambda x: x % 2, Number80))
    Number80.append(ConvertTo(max(SumCh, SumNCh), 80)[-1])

    return ConvertFrom(Number80, 80)

N = 0

while F(N) <= 1000000:
    N += 1

print(N)