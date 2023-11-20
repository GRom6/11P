from fnmatch import fnmatch

for i in range(10 ** 10, 0, -1):
    if i % 11071 == 0:
        print(i)
        break

counter = 0
for N in range(9999991460, 0, -11071):
    if fnmatch(str(N), "?136*1"):
        if int(str(N)[0]) % 2 != 0 and int(str(N)[-2]) % 2 == 0:
            print(N, N // 11071)
            counter += 1
            if counter == 5:
                break



