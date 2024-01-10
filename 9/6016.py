arr = [list(map(lambda x: int(x)**2, line.split())) for line in open("6016.txt")]
res = []

for line in arr:
    if len(line) == len(set(line)):
        if max(line) < sum(line) - max(line):
            res.append(line)

print(len(res))