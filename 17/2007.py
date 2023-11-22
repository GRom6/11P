Array = list(map(int, open("17_2007").readlines()))
Arr_Numbs = []

for i in Array:
    if i % 10 >= 4:
        if i % 3 == 0 and i % 9 != 0:
            Arr_Numbs.append(i)
print(len(Arr_Numbs), sum(Arr_Numbs)//len(Arr_Numbs))