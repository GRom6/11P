from itertools import *
n = 0
for s in product('БГДНОУШ', repeat = 6):
   n += 1
   s = ''.join(s)
   if n % 2 != 0 and s[0] != 'Б':
       if s.count('Н') >= 2 and 'У' not in s:
           print(n)
# abc = "Г, О, Н, Д, У, Б, Ш".split(", ")
# abc.sort()
# Dict_abc = {}
# for i in range(len(abc)):
#     Dict_abc[i] = abc[i]
# print(Dict_abc)
# max_number = sum([5 * (6 ** i) for i in range(6)])
#
# def convert(n):
#     res = []
#     while n:
#         res.append(n % 6)
#         n //=6
#     return res[::-1]
#
# for i in range(max_number, 0, -1):
#
#     if i % 2 == 1:
#         In6 = convert(i - 1)
#         word = []
#         for j in In6:
#             word.append(Dict_abc[j])
#         while len(word) < 6:
#             word.append('Б')
#         word = word[::-1]
#         print(word)
#
#         if word[0] != 'Б' and word.count('Н') > 1 and word.count('У') == 0:
#             print(i)
#             break

