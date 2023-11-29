Array = [int(x) for x in open('17_10771').readlines()]
Answer = []

def product(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    else:
        return True
    
for i in range(len(Array) - 2):
    flag = '3' in list(str(Array[i]))
    flag *= '3' in list(str(Array[i + 1]))
    flag *= '3' in list(str(Array[i + 2]))
    summ = sum(Array[i:i + 3])
    if flag and product(summ):
        Answer.append(summ)

print(len(Answer), min(Answer))
