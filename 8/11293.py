from itertools import product
A = list(product([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], repeat=6))
def Start0(N):
    if N[0] != 0 and (not N.count(5) > 1):
        last = N[0] % 2
        for i in range(1, len(N)):
            if last == 1 and N[i] % 2 == 1: #Не подходит в условие
                return False
            last = N[i] % 2
        else:
            return True
    else: return False
a = list(filter(Start0, A))
print(len(a))