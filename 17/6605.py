Arr = list(map(int, open("17_6605").readlines()))
res = []
def End5(N):
    if abs(N) % 10 == 5:
        return True
    return False
max_5 = max([x for x in Arr if abs(x) % 10 == 5])
print(max_5)
Max_End5 = max(filter(End5, Arr)) ** 2

for i in range(len(Arr) - 1):
    flag = End5(Arr[i]) + End5(Arr[i + 1])
    if flag == 1:
        Squa = abs(Arr[i] ** 2 - Arr[i + 1] ** 2)
        if Squa <= Max_End5:
            res.append(Squa)
print(len(res), max(res))