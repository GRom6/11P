Arr = [int(x) for x in open("17_1994.txt")]
AllProd = []

for i in range(len(Arr) - 1):
    if abs(sum(Arr[i : i + 2])) % 7 == 0 and (Arr[i] * Arr[i + 1]) > 0:
        AllProd.append(Arr[i] * Arr[i + 1])

print(len(AllProd), min(AllProd))