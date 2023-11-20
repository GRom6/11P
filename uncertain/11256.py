import fnmatch

for i in range(0, 10**9+1, 2476):
    if fnmatch.fnmatch(str(i), "?2?5554*"):
        print(i, i//2476)