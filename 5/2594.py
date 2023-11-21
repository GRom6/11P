# 2594 23:10
from  math import sqrt
# def All_del(n):
#     res = []
#     for i in range(2, n + 1, 2):
#         if len(res) > 3:
#             print("break")
#             return []
#         elif n % i == 0 :
#             res.append(i)

#     if n % 2 == 0:
#         res.append(n)
#     return res
# for i in range(113000000, 114000001):
#     delit = All_del(i)
#     if len(delit) == 3:
#         print(i, delit)

def All_Del(n):
    mas = []
    for i in range(1, int(sqrt(n)) + 1):
        if n % i == 0:
            mas.append(i)
            mas.append(n // i)
    return mas

def prime(n):
    for i in range(2, int(sqrt(n)) + 1, 1):
        if n % i == 0:
            return False
    else:
        return True
    
for i in range(113000000, 114000001):
    if i % 2 == 0 and i % 4 != 0:
        t = i // 2
        if t == int(t**0.5)**2 and prime(int(t**0.5)):
            print(i, t**0.5)
            # print(All_Del(i))
#Т.е. все чёт делители числа: 2, х//2, sqrt(x//2)