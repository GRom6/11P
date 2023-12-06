abc = sorted( list("ЦАПЛЯ"))
dictabc = {}

for i in range(len(abc)):
    dictabc[abc[i]] = str(i)

def convertTo5(n):
    res = ''
    while n:
        res += str(n % 5)
        n //= 5
    return res[::-1]

for i in range(3500):
    number = convertTo5(i)
    if len(number) > 5:
        continue
    while len(number) != 5:
        number = '0' + number
    flag_1 = number.count(dictabc['А']) <= 1
    flag_2 = number.count(dictabc['Ц']) == 2
    flag_3 = number.count(dictabc['Л']) == 0
    if flag_1 and flag_2 and flag_3:
        print(number)
        print(int(number, 5) + 1)
        break

