# Dict = {
#     '1' : 11,
#     '2' : 1,
#     '3' : 3
# }
# dict2 = {
#     '1' : 0,
#     '2' : 3
# }
# Dict |= dict2
# a = [1, 2, 3]
# b = [1, 2, 3]
# print(a | b)
d = {'spam', 'eggs', 'cheese'}
e = {'cheese', 'cheddar', 'aardvark', 'Ethel'}
d |= e
print(d, type(d))