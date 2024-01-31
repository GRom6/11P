file = (open("24/24_11954.txt").read().strip().split("Y"))


file = list(filter(lambda x: x.count('X') >= 500, file))
file = list(map(lambda x: x[x.find('X') : x.rfind('X') + 1], file))

def F(line):
    res = []
    start = 0
    End = 0
    
    while start < len(line) - 1 and End < len(line) - 1:
        Strr = line[start:End + 1]
        if Strr.count('X') < 500:
            End += 1
        if Strr.count('X') == 500:
            res.append(Strr)
            start += 1
    
    return res

a = [len(x) for x  in F(file[0])]
print(min(a))




# print(len(file[0]), file[0].count('X'))

# def Fun(Line):
#     Count_x = Line.count('X')
#     res = []

#     for i in range(Count_x - 500 + 1):
#         line = Line[i:]
#         a = [line.find('X'), line.find('X')]
    
#         for j in range(500):
#             print(line[a[1] + 1:])
#             print(line[a[1] + 1:].find('X'))
#             a[1] = line[a[1] + 1:].find('X') + a[1] + 1
            
        
#         a = [a[0] + i, a[1] + i]

#         res.append(a)
#     print(res)
    
# Strr = 'X' * 500
# Fun(Strr)



# for char in file:
#     print(X_massive)
#     if char == 'X':
#         X_massive.append(1)

#     elif len(X_massive) == 0:
#         continue

#     elif char != 'Y' and len(X_massive) > 0:
#         X_massive[-1] += 1

#     elif char == 'Y':
#         if len(X_massive) < 500:
#             X_massive.clear()
#             print("\n \n")
#         else:
#             Min = min(Min, sum(X_massive))

# print(Min, X_massive)