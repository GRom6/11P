import fnmatch
for N in range(0, 10**9+1, 8387):
    if fnmatch.fnmatch(str(N), "*75?122*"):
        print(N, N//8387)