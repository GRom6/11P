arr = list(map(int, open('17_2978')))
res = []

for i in range(len(arr) - 1):
    Summ = sum(arr[i : i + 2])**0.5
    if