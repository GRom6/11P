Arr = list(map(int, open('17_1970.txt')))
Res = []
Is_Del3 = lambda x: abs(x) % 3 == 0

for i in range(len(Arr) - 1):
    if Is_Del3(Arr[i + 1]) or Is_Del3(Arr[i]):
        Res.append(sum(Arr[i : i + 2]))
print(len(Res), max(Res))