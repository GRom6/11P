from itertools import product
a = list(product("01234", repeat = 5)) #Т.к. первое 3 - на 0 проверка не нужна, да и длинна 5

# def Chet(n):
#     N = ['3'] + [x for x in n]
#     N = int("".join(N), 5)

#     if N % 2 == 0:
#         return True
#     else:
#         return False
#a = len(list(filter(Chet, a)))

def ChetForMap(n):
    N = ['3'] + [x for x in n]
    N = int("".join(N), 5)

    if N % 2 == 0:
        return 'C'
    else:
        return 'F'

a = (list(map(ChetForMap, a))).count('C')


print(a)
