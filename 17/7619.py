Arrray = list(map(int, open("17_7619").readlines()))
def Only2symb(N):
    if N // 100 == 0:
        return True
    return False
Max_2symb = max(list(filter(Only2symb, Arrray)))
All_Par = []
for i in range(len(Arrray)-1):
    Summ_Par= Arrray[i] + Arrray[i + 1]
    flag = Only2symb(Arrray[i]) + Only2symb(Arrray[i + 1])
    if flag and Summ_Par % Max_2symb == 0:
        All_Par.append(Summ_Par)
print(len(All_Par), max(All_Par))