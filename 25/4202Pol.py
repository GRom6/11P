def prod(number):
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    else:
        return True


prost = [x for x in range(3*10**6, 10*10**6) if prod(x)]
count_pare = 0
avg_last_pare = 0
for i in range(1, len(prost)):
    if prost[i] - prost[i - 1] == 2:
        count_pare += 1
        avg_last_pare = prost[i] - 1
print(count_pare, avg_last_pare)
