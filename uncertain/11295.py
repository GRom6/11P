from itertools import product
A = list(product("ДРСЩЭ", repeat = 4))
print(A.index(("Щ", "Д", "Щ", "Д")) + 1)