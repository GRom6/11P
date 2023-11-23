Arr = list(map(int, open("17_6791").readlines()))
SumQw = []
def End68(N):
    if abs(N) % 100 == 68:
        return True
    return False

Min_End68 = min(filter(End68, Arr)) ** 2

for i in range(len(Arr) - 1):
    flag = End68(Arr[i]) + End68(Arr[i + 1])
    if flag == 1:
        SqrtSumm = Arr[i]**2 + Arr[i + 1]**2
        #QrtSumm = sum([map(lambda x: x ** 2, [Arr[i], Arr[i+1]])])
        if SqrtSumm >= Min_End68:
            SumQw.append(SqrtSumm)

print(len(SumQw), max(SumQw))