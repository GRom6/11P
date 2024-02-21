Arr = list(map(int, open("17_8954.txt")))


def is_EndInHex0F(number):
    return hex(number)[-2:] == "0f"

MaxEnd0F = max(filter(is_EndInHex0F, Arr))
print(MaxEnd0F)

res = []
for i in range(len(Arr) - 1):
    if (Arr[i] % 7 == 0) != (Arr[i + 1] % 7 == 0):
        if (Arr[i] + Arr[i + 1]) % MaxEnd0F == 0:
            res.append(Arr[i] + Arr[i + 1])
        
print(len(res), max(res))