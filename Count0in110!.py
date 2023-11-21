#count 0 in 110!
from functools import lru_cache
@lru_cache
def fact(n):
    if n == 1:
        return(1)
    return(n*fact(n - 1))

a = fact(110)
Counter = 0
print(a)
while a % 10 == 0:
    a //= 10
    Counter += 1
print(a, Counter)