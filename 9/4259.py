with open("4259") as f:
    Array = [list(map(int, line.split())) for line in f.readlines()]
    res = 0
    for line in Array:
        line_1 = line.copy()
        line_1.remove(max(line))
        line_1.remove(min(line))

        NumbsIn3 = list(map(lambda x: x**3, line_1))
        if (max(line) + min(line))**3 > sum(NumbsIn3):
            res += 1
    print(res)

