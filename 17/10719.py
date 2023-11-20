def End13(a, b):
    return (((abs(a) % 100) == 13) != ((abs(b) % 100) == 13))

f = open("17_10719").readlines()
Array = [int(i) for i in f]
ListSum = []

for i in range(len(Array) - 4):
    if End13(Array[i], Array[i+3]):
        ListSum.append(Array[i] + Array[i+3])
print(len(ListSum), max(ListSum))