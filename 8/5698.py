from itertools import permutations
PartNumb = list(permutations(map(int, list("0123456789")), r = 3))
print(PartNumb)
CounterxD = 0

def MyAny(List1, List2):
    for x in List1:
        for
for FirstPart in PartNumb:
    for SecondPart in PartNumb:
        if sum(FirstPart) == sum(SecondPart):
            if FirstPart != SecondPart:
                if any(FirstPart) == any(SecondPart):
                    CounterxD += 1
                    if FirstPart == (1, 5, 6) and SecondPart == (6, 2, 4):
                        print('True')
print(CounterxD)