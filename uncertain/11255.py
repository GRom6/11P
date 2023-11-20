from fnmatch import fnmatch

for i in range(0, 10**10+1, 7157):
    if fnmatch(str(i), "*3185*32"):
        print(i, i//7157)