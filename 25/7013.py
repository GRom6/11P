#7013 22:45
from math import *
from functools import lru_cache
from itertools import product
from fnmatch import fnmatch

@lru_cache
def All_Del(n):
    mas = []
    for i in range(1, int(sqrt(n)) + 1):
        if n % i == 0:
            mas.append(i)
            mas.append(n // i)
    return mas

def Count_Del(Count_del):
    degree = 0
    while Count_del > 2 ** degree:
        degree += 1
    if Count_del == 2 ** degree:
        return True
    return False

Answer = []
for i in range(0, 10**9 - 1, 677):
    if fnmatch(str(i), "*31*65?"):
        All_del = All_Del(i)
        if (31 in All_del) and (2031 in All_del):    
            if Count_Del(len(All_del)):
                Answer.append([i, i // 2031])

for One in Answer:
    print(One)
#23:04


#print(All_Del(31), All_Del(2031)) #31   // 2031, 3, 677

        