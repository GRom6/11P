def ConvertTo4(n):
    res = ""
    while n:
        res += str(n % 4)
        n //= 4
    return res[::-1]


Answer = []
for i in range(1, 100000):
    R = ConvertTo4(i)
    R = str((i % 2)) + R + str((i % 3))

    R_int = int(R, 4)
    if R_int < 100 and R_int > 9:
        Answer.append(R_int)
        
print(max(Answer))
