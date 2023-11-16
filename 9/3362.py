with open("3362.txt") as file:
    Array = [list(map(int, line.split())) for line in file.readlines()]

    answer = 0
    for line in Array:
        Chet = sum([x for x in line if x % 2 == 0])
        NChet = sum([x for x in line if x % 2 != 0])

        if NChet > Chet:
            answer += 1
            
    print(answer)