Arr = [list(map(int, line.split())) for line in open("9-191.txt")]
counter = 0

def SrArth(bList):
    return sum(bList) / len(bList)

for line in Arr:
    Rep = [x for x in line if line.count(x) > 1]
    UnRep = [x for x in line if line.count(x) == 1]
    if len(Rep) > 0 and len(UnRep) > 0:
        counter += SrArth(Rep) > SrArth(UnRep)