from itertools import product
Sogl = "АИУОЯ"
Glas = "НТП"
def counts(str1, list_char):
    res = 0
    for i in list_char:
        res += str1.count(i)
    return res


def Filter_End(str1):
    Sogl = "АИУОЯ"
    Glas = "НТП"
    return  counts(str1, Sogl) == counts(str1, Glas)

def Filter_Start(str1):
    Glas = "НТП"
    return (counts(str1, Glas) <= 2)


end_TOTAl = list(filter(Filter_End, list(product(Sogl+Glas, repeat = 6))))
end_Mid = list(filter(Filter_End, list(product(Sogl+Glas, repeat = 4))))
end_Min = list(filter(Filter_End, list(product(Sogl+Glas, repeat = 2))))


start_Total = list(filter(Filter_Start, list(product(Sogl+Glas, repeat = 6))))
start_Mid = list(filter(Filter_Start, list(product(Sogl+Glas, repeat = 4))))
start_Min = list(filter(Filter_Start, list(product(Sogl+Glas, repeat = 2))))

print(start_Min)

res  = len(end_TOTAl) * 1
res += len(end_Mid)   * len(start_Min)
res += len(end_Min)   *  len(start_Mid)
res += len(start_Total) * 1

print(res)