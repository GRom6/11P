from math import factorial
LineToPallind = "Лёшанаполкеклопанашёл".lower()

print(*(x for x in LineToPallind if LineToPallind.count(x) == 1))
print(len(LineToPallind))

#25 => 12 'е' 12. Second 12 are same with first

AllSimb = []
OnseWasRegreted = []

for Char in LineToPallind:
    if Char not in OnseWasRegreted:
        AllSimb.append(Char)
        OnseWasRegreted.append(Char)

    elif Char in OnseWasRegreted:
        OnseWasRegreted.remove(Char)

AllSimb.remove('е')

AllCountPermutation = factorial(len(AllSimb))

for RepeatChat in set([x for x in AllSimb if AllSimb.count(x) > 1]):
    AllCountPermutation = AllCountPermutation / factorial(AllSimb.count(RepeatChat))
print(AllCountPermutation)
