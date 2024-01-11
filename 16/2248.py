from functools import lru_cache
from sys import setrecursionlimit
setrecursionlimit(2000)

@lru_cache(128)
def F(n):
    if n <= 1:
        return n
    elif n % 3 == 0 and n > 1:
        return int(n + F(n//3))
    else:
        return int(n + F(n + 3))

for n in range(100):
    try:
        F_n = F(n)
    except:
        continue
    if F_n > 100:
        print(n)
        break