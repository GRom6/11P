Line = open("24_21.txt").read().strip()
LastCh = ""
Act, Max = 0, 0

for Char in Line:
    if Char == LastCh:
        Max = max(Max, Act)
        Act = 0
    Act += 1
    LastCh = Char
print(Max, Act)