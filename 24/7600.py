Line = open("24_7600.txt").read().strip()
LastCh = "O"
Act, Max = 0, 0

for Char in Line:
    if Char in "QRS" and LastCh in "QRS":
        Max = max(Max, Act)
        Act = 0
        LastCh = 'O'

    if Char in "QRS" and LastCh not in "QRS":
        LastCh = Char
        Act += 1

    else:
        Act += 1
        LastCh = "O"

print(Max, Act)