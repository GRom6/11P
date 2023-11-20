from itertools import product
SysSchet = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
a = list(product(SysSchet, repeat = 5))
def If(N):
    IndexF6 = N.index(6)
    es = 0
    flag = N[N.index(6) + 1] % 2 != 0
    if IndexF6 != 0:
        flag += N[N.index(6) - 1] % 2 != 0
    else:
        es +=1

    S = N.index(6) + 1 #StartToSearchSec
    flag += N[N.index(6, S) - 1] % 2 != 0

    if N[-1] == 6:
        es += 1
    else:
        flag += N[N.index(6, S) + 1] % 2 != 0

    return (flag + es == 4)

Answer = 0
for N in a:
    if N[0] == 0 or N.count(6) !=2:
        continue
    if If(N):
        Answer+=1
print(Answer)
