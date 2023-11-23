print(" a  b  c  t")
#c t a b
def If (a, b, c, t):
    if (not a or not b) and (c <= (not a)) and (t and not a or c and not b):
        return True
    else:

        return False

for i in range(4):
    l = [1, 0]
    if not If(0, 1, l[0], l[1]):
        print("c = 1, t = 0")
    else:
        print("c = 0, t = 1")
