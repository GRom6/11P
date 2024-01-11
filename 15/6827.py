P = range(257, 1001)
Q = range(5, 101)
R = range(99, 259)

res = []
for Astart in range(1101):
    for Aend in range(Astart, 1102):
        A = range(Astart, Aend)
        for x in range(1010):
            if not (((x in A) <= (x in R)) and (not ((x in A) <= (x in P)) <= (x in Q))):
                break
        else:
            print(A)
            res.append(len(list(A)))

print((res))
#Без понятия почему((