Line = open("24_105.txt").read().strip()

LastChar = 'o'
Act, Max = 0, 0
for Char in Line:
    if LastChar != Char:
        Max = max(Max, Act)
        Act = 0
    LastChar = Char
    Act += 1
print(Max, Act)