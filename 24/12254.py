F = list(open("24/24_12254.txt").read())

Max, Act, LastChar = 0, 0, 'T'
Line = list("RSQ")
for Char in F:
    if LastChar == 'T':
        LastChar = Char
        Act = 1
        continue

    IndexLastCharLine = Line.index(LastChar)
    if IndexLastCharLine == 2: IndexLastCharLine = -1
    if Char == Line[IndexLastCharLine + 1]:
        Act += 1
    else:
        Max = max(Act, Max)
        Act = 1

    LastChar = Char
    
print(Max, Act, LastChar)