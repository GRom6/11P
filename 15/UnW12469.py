res = []
D = range(7, 69)
C = range(29, 101)

for Ast in range(101):
    for Aend in range(Ast, 1000):
        A = range(Ast, Aend + 1)
        for x in range(120):
            if (((x in D) <= ((not x in C) and (not x in A))) <= (not x in D)):
                pass
            else:
                break
        else:
            res.append(len(list(A)))

print(min(res))