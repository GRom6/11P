f = [st.split()[0] for st in open("ip_list").readlines()]


Dictt = {}
for ipp in f:
    if ipp in Dictt:
        Dictt[ipp] += 1
    else:
        Dictt[ipp] = 1

MaxEl = [0, 0]
for i in Dictt.keys():
    if Dictt[i] >= MaxEl[1]:
        MaxEl[0], MaxEl[1] = i, Dictt[i]
print(MaxEl[0])