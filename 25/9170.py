from fnmatch import fnmatch
from math import sqrt

# def All_Del(N):
#     result = []
#     for i in range(1, int(sqrt(N)) + 1):
#         if N % i == 0:
#             result.extend([i, N//i])
#     return result

def All_Del_End_4(N):
    result = []
    for i in range(1, int(sqrt(N))+1):
        if N % i == 0:
            if str(i)[0] == '4':
                result.append(i)
            if str(N//i)[0] == '4':
                result.append(N//i)
    return result


for N in range(10**6):
    All_del = All_Del_End_4(N)
    if len(All_del) == 24:
        print(N, max(All_del))