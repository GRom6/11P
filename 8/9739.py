from itertools import product
A = list(product(sorted("МАНГУСТ"), repeat = 6))
for i in range(len(A)-1, 0, -1):
    if A[i][0] !='У' and A[i].count('М') == 2 and A[i].count('Г') <= 1:
        print(i+1)
        break