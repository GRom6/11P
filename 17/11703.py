Arr = [int(number) for number in open("17_11703.txt")]

def is_FiveDigit(number):
    if abs(number) >= 10000 and abs(number) <= 99999:
        return True
    return False

MaxEnd18 = max(filter(lambda x: abs(x) % 100 == 18, Arr))

CurrTh = []

for i in range(len(Arr) - 2):
    if (Arr[i] * Arr[i + 1] * Arr[i + 2]) % MaxEnd18 == 0:
        if is_FiveDigit(Arr[i]) + is_FiveDigit(Arr[i + 1]) + is_FiveDigit(Arr[i + 2]):
            CurrTh.append(Arr[i] * Arr[i + 1] * Arr[i + 2])
print(len(CurrTh), max(CurrTh))