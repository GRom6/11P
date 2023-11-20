from itertools import product
SysSchet = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
a = list(product(SysSchet, repeat = 4))

def FForFilter(N):
    if N[0] != 0 and N.count(9) == 1:
        last = N[0] % 2
        for i in range(1, len(N)):
            if N[i] % 2 == last:
                return False
            else:
                last = N[i] % 2
        else:
            return True
    return False

A = list(filter(FForFilter, a))
print(len(A))