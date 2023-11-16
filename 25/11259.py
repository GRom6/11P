from fnmatch import fnmatch

for i in range(3226, 10 ** 8 + 1, 3226):
    if fnmatch(str(i), '3?99?7*8'):
        print(i, i // 3226)