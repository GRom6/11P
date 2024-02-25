Arr = [list(map(int, line.split())) for line in open("6563PolT")]

count = 0
for line in Arr:
    line.remove(max(line))

    MinEl = min(line)
    line.remove(MinEl)

    if line[0] * line[1] % MinEl == 0:
        count += 1
print(count)