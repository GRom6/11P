Array = list(map(int, open("17_2012").readlines()))
Arr_Numbs = []
for i in Array:
    flag = i % 2 == 0
    flag += i % 3 == 0
    flag += i % 5 == 0
    flag += i % 7 == 0
    if flag == 2:
        Arr_Numbs.append(i)
print(len(Arr_Numbs), min(Arr_Numbs) + max(Arr_Numbs))