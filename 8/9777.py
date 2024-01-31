from itertools import product

Alf = sorted("КОМПЬЮТЕР")

AllWord = list(product(Alf, repeat = 5))

MatchFor = list(filter(lambda x: x[0] != 'Ь' and x.count('К') == 2, AllWord))

AllIndex = [AllWord.index(x) for x in MatchFor]
print(max(filter(lambda x: x % 2 == 0, AllIndex)) + 1)