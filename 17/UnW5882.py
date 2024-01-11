arr = list(map(int, open("17_5882.txt")))
E3 = lambda x: '3' in str(x)

End3 = list(filter(E3, arr))
min_el = 100000
for i in range(len(arr) - 1):
    if E3(arr[i]) != E3(arr[i + 1]):
        min_el = min(min_el, arr[i + 1], arr[i])
        print(min_el, arr[i + 1], arr[i])

print(min_el)
min_el = sum(list(map(lambda x: int(x)**2, list(str(abs(min_el))))))

print(min_el)
End3 = list(filter(lambda x: int(x) >= min_el, End3))
print(len(End3), min(End3))
