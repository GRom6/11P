arr = list(map(int, open("17_6024.txt")))
End12 = lambda x: x % 100 == 12
Max_el = max(filter(End12, arr)) ** 2
res = []

for i in range(len(arr) - 1):
    if End12(arr[i]) != End12(arr[i + 1]):
        if sum(arr[i: i + 2])**2 < Max_el:
            res.append(sum(arr[i: i + 2]))
print(len(res), max(res))