from math import *

def All_Del(N):
    result = [1]
    for i in range(2, int(sqrt(N))+1):
        if N % i == 0:
            result.append(i)
            if i == N//i:
                break
            result.append(N//i)
    return result

def Prost(N):
    for i in range(2, int(sqrt(N)) + 1):
        if N % i == 0:s
            return False
    else:
        return True

def FofA(N):
    A = list(filter(Prost, All_Del(N)))
    A = sum(A) / len(A)
    return round(A)

N = 310002
result = []
while len(result) < 6:
    if FofA(N) % 10 != 4 and FofA(N) % 6 == 0:
        result.append([N, FofA(N)])
        N += 6
    else:
        N += 6

print(result)