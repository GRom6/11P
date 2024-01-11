for x in range(9, 20):
    for y in range(8, 20):
        if int("87", x) == int("73", y):
            if int("62", x) == int("52", y):
                print(str(max(x, y)) + str(min(x, y)))
                break