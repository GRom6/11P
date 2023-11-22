array = [list(map(int, line.split())) for line in open("5707").readlines()]
res = 0
for line in array:
    Ar_Min = list(map(lambda x: x**2, sorted(line)[0:3]))
    Ar_Max = sorted(line)[3:6]
    if sum(Ar_Min) > (Ar_Max[0] * Ar_Max[1] * Ar_Max[2]):
        res += 1

print(res, "Зря на проверку время убил")


