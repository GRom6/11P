Arr = [list(map(int, line.split())) for line in open("5909PolT")]

res = []
for line in Arr:
    if max(line)**3 > (line[0] * line[1] * line[2] * line[3] * line[4]):
        res.append(line)

print(len(res))
