from functools import lru_cache
from sys import setrecursionlimit
setrecursionlimit(1000)

# 3 6 9 12 15
@lru_cache()
def Fact(x):
    if x == 1:
        return 1
    return (x * Fact(x - 1))

answ = 0
for i in range(3, 16, 3):
    answ += Fact(15)/(Fact(i - 1)*Fact(16 - i)) #С i - 1, и начиная с 15 т.к. 1я всегда 1ца.
    #fact(i - 1) за повторение едениц, а Fact(16 - i) - за 0и
print(answ)