#z w y x
for x in range(2):
    for y in range(1, 2):
        for z in range(2):
            for w in range(1, 2):
                if not((z<= w) and y and not x):
                    print(x, y, z, w)