Array = [list(map(int, line.split())) for line in open("4755").readlines()]

result = 0 
for line in Array:
    NPovt = [x for x in line if line.count(x) == 1]
    Povt = [x for x in line if line.count(x) == 2]

    if Povt != []:
        for x in Povt:
            for y in NPovt:
                if x < y:
                    break
            else:
                continue
            break
        else:
            result += 1
print(result)