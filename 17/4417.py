Arr = [int(number) for number in open("17_4417.txt")]

res = []
for i in range(len(Arr) - 1):
    for j in range(i, len(Arr)):
        if (Arr[i] + Arr[j]) % 120 == 0:
            res.append(Arr[i] + Arr[j])
print(len(res), max(res))