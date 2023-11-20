from itertools import product
A = list(product("01234567", repeat = 5))
a = [list(map(int, line)) for line in A]
def FFilter(N):
    Collis = [x for x in N if N.count(x) != 1]
    if N[0] != 0 and N.count(1) == 0 and len(Collis) == 0:
        last = N[0] % 2
        for i in range(1, len(N)):
            if N[i] % 2 == last:
                return False
            else:
                last = N[i] % 2
        else:
            return True

res = list(filter(FFilter, a))
print(len(res))
