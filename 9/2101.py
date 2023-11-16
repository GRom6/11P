Array = [list(map(int, line.split())) for line in open("2101.txt").readlines()]

result = 0

for line in Array:

    if max(line)**2 < min(line)**2 + (sum(line) - max(line) - min(line))**2:
        result += 1

print(result)