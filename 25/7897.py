result = [0,0,0,0,0]

#Да, в идеале с макс по мин искать... но мне так лень переделывать, простите
for i in range(0, 9136999981, 11071): #На 11071*10 т.к. на конце 1ца
    n = str(i)
    if n[-1] == '1' and n[1:4] == '136' and int(n[0]) % 2 and (not int(n[4:len(n)-1]) % 2): #fnmatch 7897-человека
        result.pop(0)
        result.append([i, i//11071])

for i in range(5):
    print(result[i][0], result[i][1])