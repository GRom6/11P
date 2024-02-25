count = 0
for line in open("6454PolT"):
    line = list(map(int, line.split()))
    if line.count(max(line)) == 1:
        RepN = list(filter(lambda x: line.count(x) > 1, line))
        if len(RepN):
            if (max(line) + min(line)) > sum(RepN): 
                count += 1

print(count)
