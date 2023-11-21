from itertools import product
Glas = "ОУАЮУ"
#a = list(permutations("ХОЧУНАБЮДЖЕТ", r = 12))
a = list(product("GS", repeat=12))
r = 0
r_1 = 0
for i in a:
    if i.count("S") == 7:
        r_1 += 1
        flag = True
        for j in range(12-4):
            if i[j] == i[j+1] == i[j+2] == i[j+3] == i[j+4] == "S":
                flag = False
        if flag:
            r += 1
print(r, r_1, len(a))