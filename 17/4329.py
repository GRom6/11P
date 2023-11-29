Array = [int(x) for x in open('17_4329').readlines()]
Answer = [0, 0]

def delit(n):
    res = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            res.append(i)
            res.append(n // i)
    return res

max_del= []
for n in Array:
    act_del = delit(n)
    if len(act_del) > len (max_del):
        max_del = list(act_del)


def F(delit_n):
    answ = 0
    for i in delit_n:
        if i in max_del:
            answ += 1
 
    return answ

for i in range(len(Array)-1):
    delit_n1 = delit(Array[i])
    delit_n2 = delit(Array[i + 1])
    flag = F(delit_n1) >= 3
    flag *= F(delit_n2) >=3
    if flag:
        Answer[0] += 1
        General_del = 0
        for d in delit_n1:
            if d in delit_n2:
                General_del += 1
        if Answer [1] < General_del:
            Answer [1] = General_del
print(Answer)