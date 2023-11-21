def In3(n):
    return('3' in str(n))

def prime(N):
    for i in  range(2, N//2):
        if N % i == 0:
            return False
    else:
        return True

Array = [int(i) for i in open("17_10771").readlines()]
res = []
for i in range(len(Array)-2):
    summ = Array[i] + Array[i+1] + Array[i+2]

    if In3(Array[i]) and In3(Array[i+1]) and In3(Array[i+2]) and prime(summ):
       res.append(summ)

print(len(res), min(res))