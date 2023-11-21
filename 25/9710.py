from fnmatch import fnmatch
def F(N):
    return sum(map(int, str(N)))

def Chast(N):
    return (N//2023)

Array = [x for x in range(999999245, 2*(10**9), 2023) if fnmatch(str(x), "1*1")]

Array.sort(key=F, reverse=True)
Array = list(map(Chast, Array))
Array = sorted(Array[:5])

for item in Array:
    print(item)

# FiveWithMaxSum = []
#
# for N in Array:
#     if len(FiveWithMaxSum) < 5:
#         FiveWithMaxSum.append([N, F(N)])
#     else:
#         SummActN = F(N)
#         for i in range(len(FiveWithMaxSum)):
#             if SummActN > FiveWithMaxSum[i][1] or (SummActN == FiveWithMaxSum[i][1] and N > FiveWithMaxSum[i][0]):
#                 FiveWithMaxSum[i] = [N, SummActN]
#
#
# print(FiveWithMaxSum)
#
# for i in range(len(FiveWithMaxSum)):
#     FiveWithMaxSum[i] = FiveWithMaxSum[i][0] // 2023
#
# FiveWithMaxSum.sort()
#
# for i in range(len(FiveWithMaxSum)):
#     print(FiveWithMaxSum[i])
