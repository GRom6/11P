def F(n):
    bin_n = bin(n)[2::]
    
    if len(bin(n % 3)[2::]) < 2:
        bin_n += '0' + bin(n % 3)[2::]
    else:
        bin_n += bin(n % 3)[2::]
    
    bin_n += '0' * (3 - len(bin(n % 5)[2::])) + bin(n % 5)[2::]
    return int(bin_n, 2)

print(45138888 - 34722222 + 1)
print(int(bin(1111111110)[2:-5], 2))
res = []
for n in range(34722222,45138889):
    x = F(n)
    if x in range(1111111110, 144444444416) and x not in res:
        res.append(x)
print(len(res))
#idea Число увеличивается в 2*
