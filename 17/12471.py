zxc = list(map(int, open("17/17_12471.txt")))
MaxElEnd1 = max(filter(lambda x: str(x)[-2:] == '13', zxc))

res = []
for i in range(len(zxc) - 2):
    flag1 = all(map(lambda x: x % 2 == 0, zxc[i:i+3]))
    flag2 = any([len(str(x)) == 2 for x in zxc[i:i+3]])
    Summ = sum(zxc[i:i+3])
    if (flag1 or flag2) and Summ <= MaxElEnd1:
        res.append(Summ)

print(len(res), sum(res)//len(res))