Array = [int(line) for line in open("/home/kosuma/Документы/School/11P/17/17_9547").readlines()]


def F3(n):
    if n < 1000 and n > 99:
        return True
    else:
        return False
Min_el = min([x for x in list(filter(F3, Array)) if x % 100 == 11])
res = []
for i in range(len(Array) - 1):
    flag_1 = F3(Array[i])
    flag_2 = F3(Array[i + 1])
    Dif = abs(Array[i] - Array[i + 1])
    if flag_1 != flag_2 and Dif % Min_el == 0:
        res.append(Array[i] + Array[i + 1])
print(len(res), max(res))