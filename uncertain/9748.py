Array = list(map(int, open("17_9748").readlines()))
def End15(n):
    return n % 100 == 15

Max = max(filter(End15, Array))

result = []

for i in range(len(Array) - 2):
    summ = Array[i] + Array[i+1] + Array[i+2]
    flag =  len(list(str(Array[i])))     == 4
    flag += len(list(str(Array[i + 1]))) == 4
    flag += len(list(str(Array[i + 2]))) == 4

    if (flag == 1) and (summ >= Max):
        result.append(summ)
        
print(len(result), max(result))