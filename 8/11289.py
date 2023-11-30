from itertools import permutations
arr = list(permutations("87654310", r=7))
def Filt0(List):
    if List[0] == '0':
        return False
    Ch_last = 2
    for i in List:
        if Ch_last != int(i) % 2:
            Ch_last = int(i) % 2
        else:
            return False
    return True
arr = list(filter(Filt0, arr))
print(len(arr))