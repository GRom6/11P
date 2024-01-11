from functools import lru_cache
from sys import setrecursionlimit
setrecursionlimit(2000)

@lru_cache(128)
def F(n):
    if n == 2:
        return 2
    elif n == 1:
        return 1
    elif n % 2 == 0 and n > 2:
        return int((((n + F(n - 2))) / 5))
    else:
        return int(((2*n + F(n - 1) + F(n - 2)) / 4))
    
print(F(50))
    
