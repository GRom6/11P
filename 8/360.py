from itertools import product

Glas = sorted(list("ИА"))
Sogl = sorted(list("НСТВК"))
Abc =  sorted(Glas + Sogl)

def Filt(st):
    if st[0] in Sogl and st[-1] in Glas:
        return True
    return False

Array = list(product(Abc, repeat = 4))
Arr = list(filter(Filt, Array))
answer = Arr.index(('Н','И','К','А')) + 1
print(answer)