Array = list(map(int, open("17_7848").readlines()))
def FirstIf(N):
    N = list(map(int, list(str(N))))
    for i in range(len(N)-1):
        if not N[i]<N[i+1]:
            return False
    else:
        return True

def ThirdIf(N):
    N = list(map(int, list(str(N))))
    a = N.copy()
    a = sorted(list(set(a)))
    return (N[::-1] == a)


MinElemelemt = min(list(filter(ThirdIf, Array)))  #Минимальный элемент со строгой обратной последовательностью цифра

result = []
for i in range(len(Array)-1):
    if FirstIf(Array[i]) != FirstIf(Array[i+1]):
        if Array[i]*Array[i+1] % sum(list(map(int, list(str(MinElemelemt))))) == 0: #Произведение кратно сумме цифр MinElemelemt
            result.append(Array[i] + Array[i+1])

print(len(result), min(result))


