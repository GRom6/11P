Line = open('24_3020.txt').read().strip().replace("ZX", '1').replace("ZY", '1')

Act, Max = 0, 0

for char in Line:
    if char == '1':
        Act += 1

    else:
        Max = max(Max, Act)
        Act = 0

print(max(Act, Max))