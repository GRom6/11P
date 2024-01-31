Alf = sorted("ШКОЛА")

from itertools import product
List = list(product(Alf, repeat = 5))

print(List.index(('Ш', 'А', 'Л', 'А', 'Ш')) + 1)