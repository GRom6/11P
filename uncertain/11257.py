from fnmatch import fnmatch
for i in range(0, 10**9, 6718):
    if fnmatch(str(i), "?46?44*2"):
        print(i, i//6718)