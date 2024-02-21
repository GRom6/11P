Arr = list(map(int, open("17_8504.txt")))

is_ThreeDigit = lambda x: x > 99 and x < 1000
MinThreeDigit = min(filter(is_ThreeDigit, Arr))

res = []
for i in range(len(Arr)-1):
    if is_ThreeDigit(Arr[i]) or is_ThreeDigit(Arr[i + 1]):
        if (Arr[i] + Arr[i + 1]) %  MinThreeDigit == 0:
            res.append(Arr[i] + Arr[i + 1])

print(len(res), max(res))