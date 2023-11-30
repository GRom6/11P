from itertools import product
arrr = product([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], repeat = 8)
count = 0
for i in arrr:
    if i.count(10) <= 2 and len(set(i)) == 6:
        count += 1
print(count)
