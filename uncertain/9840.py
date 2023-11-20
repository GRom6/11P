file = list(map(int, open("17_9804").readlines()))
result = []
Need = max([a for a in file if len(str(abs(a))) == 4 and abs(a) % 100 == 39])
for n in range(len(file)-1):
    summ = file[n] + file[n+1]
    flag = ((summ**2) <= (Need**2))

    if (len(str(abs(file[n]))) == 4) != (len(str(abs(file[n+1]))) == 4) and flag:
        result.append(summ)
print(len(result), max(result))