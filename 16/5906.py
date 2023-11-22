from functools import lru_cache
from sys import setrecursionlimit
setrecursionlimit(1000000)
@lru_cache
def F(x, y):
    if x == 0:
        return (y + 1)
    if y == 0:
        return (F(x-1, 1))
    return (F(x-1, F(x, y - 1)))

print(F(3, 11))