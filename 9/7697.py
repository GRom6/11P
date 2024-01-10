Arr = [list(map(int, line.split())) for line in open("7697.txt")]
res = 0

for line in Arr:
    if sum(line) % 18 == 0: #т.к. все числа равны 18 - всегда длятся на 5
        res += 1

print(res)