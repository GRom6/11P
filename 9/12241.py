Array = [list(map(int, line.split())) for line in open("12241.txt")]
res = []

for line in Array:
    RepeatNumb = [x for x in line if line.count(x) == 2]
    NotRepeat = [x for x in line if line.count(x) == 1]
    
    if not RepeatNumb:
        continue

    Summ = (max(RepeatNumb) + min(RepeatNumb)) / 2
    if len(RepeatNumb) == 6 and Summ < NotRepeat[0]:
        res.append(line)
print(len(res))