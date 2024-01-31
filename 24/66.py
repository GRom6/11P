Line = open("24_66.txt").read().strip().replace("KOT", '1')
Act, Max = 0, 0
for Item in Line:
    if Item.isdigit():
        Act += int(Item)
    else:
        Max = max(Act, Max)
        Act = 0
print(Max, Act)