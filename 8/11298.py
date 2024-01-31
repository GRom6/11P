Alf = sorted("АОЖПЮЗ")

from itertools import product
List = list(product(Alf, repeat = 6))

Res = 0
for i in range(1, len(List), 2):
    line = List[i]
    if line[0] == 'А' and line.count('З') >= 2:
        Res += 1
print(Res)