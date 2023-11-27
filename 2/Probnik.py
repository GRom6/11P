def F(x, y, z, w):
    flag_1 = (x == y) and (x <= z)
    flag_2 = (x<=y)<=(w==z)
    return([flag_1, flag_2])
a = [[],[],[]]
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                ff = F(x, y, z, w)
                if ff[0] == True and ff[1] == False and x+y+z+w >=3:
                    a[0].append([x, y, z, w])
                if ff[0] == True and x+y+z+w<=2:
                    a[1].append([x, y, z, w])
                if ff[0] == False and ff[1] == False and x+y+z+w<3:
                    a[2].append([x, y, z, w])           
for i in range(3):
    print(a[i])
