from itertools import permutations
PartNumb = list(permutations(map(int, list("0123456789")), r = 3))

CounterxD = 0

for FirstPart in PartNumb:
    for SecondPart in PartNumb:
        if SecondPart != FirstPart:
            if sum(FirstPart) == sum(SecondPart):
                
                for NumbF in FirstPart:
                    for NumbS in SecondPart:
                        if NumbF == NumbS:
                            break
                    else:
                        continue
                    CounterxD += 1
                    break
print(CounterxD)