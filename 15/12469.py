D = range(7, 68 + 1)
C = range(29, 100 + 1)
res = []

for StartA in range(1000):
    for EndA in range(StartA - 1, 1100):
        A =  range(StartA, EndA + 1)
        
        for x in range(1000):
            if not ((x in D) <= (((not x in C) and (not x in A)) <= (not x in D))):
                break
        else:
            res.append(len(A))
        

print(min(res))


