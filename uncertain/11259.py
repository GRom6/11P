from fnmatch import fnmatch

for number in range(0,  10 ** 8, 3226):
    if fnmatch(str(number), "3?99?7*8"):
        print(number, number // 3226)