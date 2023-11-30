def prod(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    else:
        return True
prost =  []
for i in range(3000000, 10000000):
    if prod(i):
        prost.append(i)
count_pare = 0
avg_last_pare = 0
for i in range(len(prost)):
    if prost[i] - prost[i-1] == 2:
        count_pare += 1
        avg_last_pare = prost[i] - 1
print(count_pare, avg_last_pare)