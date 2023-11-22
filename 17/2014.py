Array = list(map(int, open("17_2014").readlines()))
Arr_Numbs = []

def convert(N, to):
    res = ''
    while N:
        res += str(N % to)
        N //= to
    return res[::-1]
for i in Array:
    if convert(i, 5)[-1] == '3':
        if convert(i, 9)[-1] == '5':
            if convert(i, 8)[-1] != '7':
                Arr_Numbs.append(i)
print(len(Arr_Numbs), max(Arr_Numbs))