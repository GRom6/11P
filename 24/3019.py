Line = open('24_3019.txt').read().strip()

res = 0

for i in range(len(Line)):
    for j in range(i, len(Line)):
        if j - i > 14: #Т.к. индексы. В срезе + 1 будет:
            break
        
        if Line[i] == 'A' and Line[j] == 'B':
            UnderLine = Line[i : j + 1]
            if 'F' in UnderLine and UnderLine.count('B') == 1 and UnderLine.count('A') == 1:
                res += 1

print(res)
