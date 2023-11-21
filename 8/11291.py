from itertools import  product
a = list(product([0, 1, 2, 3, 4, 5], repeat = 7))

res = 0
for N in a:
    if N.count(2) != 1 or N[0] == 0:
        continue

    Index2 = N.index(2)
    flag = True

    if Index2 == 0:
        if N[Index2 + 1] % 2 == 0:
            flag = False
    elif Index2 == len(N) - 1:
        if N[Index2 - 1] % 2 == 0:
            flag = False

    else:
        if N[Index2 + 1] % 2 == 0:
            flag = False
        if N[Index2 - 1] % 2 == 0:
            flag = False

    if flag: res += 1

print(res)