#x z w y
def If(x, y, z, w):
    if not (((x == z) or not (x == w)) and ((y <= x) or not z)):
        return True
    return False
print("x y z w")
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if If(x, y, z, w):
                    print(x, y, z, w)