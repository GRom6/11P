Arr = list(map(int, open("17_4474.txt")))

MinMultiple103 = min(filter(lambda x: x % 103 == 0, Arr))

res = []
for i in range(len(Arr) - 1):
    if (Arr[i] + Arr[i + 1]) % 2 == 0:
        if abs(Arr[i] - Arr[i + 1]) % MinMultiple103 == 0:
            res.append(Arr[i] + Arr[i + 1])

print(len(res), max(res))