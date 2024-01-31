Arr = list(map(int, open("17_2004.txt")))
def is_Uslov(number):
    return (number % 13 == 4 and number % 8 == 1)
AllNumb = list(filter(is_Uslov, Arr))
print(max(AllNumb), sum(AllNumb))