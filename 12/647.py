def Prog(Strr):
    while '111' in Strr:
        Strr = Strr.replace('111', '2')
        Strr = Strr.replace('222', '1')
    return Strr

for i in range(30, 100):
    line = '1'*i

    if Prog(line) == '211':
        print(i)
        break

print("out")