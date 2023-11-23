def If(c, a, d, b, orer):
    if orer == "and":
        return ((a and b == (not c)) and (b and d))
    if orer == "==":
        return ((a and b == (not c)) and (b == d))
    if orer == "<=":
        print((a and b == (not c)) and (b <= d))
        return ((a and b == (not c)) and (b <= d))
    if orer == "or":
        return ((a and b == (not c)) and (b or d))

x = ["and", "==", "<=", "or"]
for i in range(1):
    flag = If(1, 0, 0, 0, x[2])
    flag += If(1, 0, 1, 0, x[2])
    flag += If(1, 0, 1, 1, x[2])
    flag += If(1, 1, 0, 0, x[2])
    if flag == 4:
        print(i + 1)