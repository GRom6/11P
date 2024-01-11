file = open("/home/kosuma/Документы/School/11P/27/27-AWithTrFirst.txt").readlines()
Nstr = int(file[0])
file.pop(0)

CurrIf = list(map(lambda x: file.index(x), filter(lambda x: (int(x) > 0 and int(x) % 2 == 0), file)))

