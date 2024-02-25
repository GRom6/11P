Arr = [list(map(int, line.split())) for line in open("6196PolT")]

count = 0
for line in Arr:
    flag1 = len(line) - len(set(line)) == 1

    SrArNCh = [int(x) for x in line if x % 2]

    if len(SrArNCh): SrArNCh = sum(SrArNCh) / len(SrArNCh) 
    else: SrArNCh = 0


    SrArCh = [int(x) for x in line if x % 2 == 0]
   
    if len(SrArCh): SrArCh = sum(SrArCh) / len(SrArCh)
    else:SrArCh = 0


    flag2 = abs(SrArNCh - SrArCh) > 50

    if flag1 != flag2:
        count += 1

print(count)