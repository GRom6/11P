arr = list(map(int, open('17_2992')))
res = []
def If(n):
    res = ''
    while n:
        res += str(n % 7)
        n //= 7
    res = res[::-1]
    return (res.find('36') != -1)

Max_el_107 = max([x for x in arr if not x % 107])

for i in range(len(arr) - 1):
    flag_1 = arr[i] > Max_el_107
    flag_1 += arr[i + 1] > Max_el_107
    flag_2 = If(arr[i]) + If(arr[i + 1])
    if flag_1 and flag_2:
        res.append(sum(arr[i : i + 2]))
print(len(res), min(res))

