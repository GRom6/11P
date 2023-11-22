Array = list(map(int, open("17_2238").readlines()))
Arr_Numbs = []
Sr_Ariph = sum(Array) / len(Array)

for i in range(len(Array) - 2):
    flag = Array[i] > Sr_Ariph
    flag += Array[i+1] > Sr_Ariph
    flag += Array[i+2] > Sr_Ariph
    if flag >= 2:
        summ = Array[i] + Array[i + 1] + Array[i + 2]
        Arr_Numbs.append(summ)

print(len(Arr_Numbs), max(Arr_Numbs))