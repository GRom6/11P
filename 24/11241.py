# s = open('24_11241.txt').readline().strip()
# for el in 'ABCD': s = s.replace(el, ' ')
# print(max(len(c) for c in s.split()))
f = open('24_11241.txt').readline().strip()
for el in "ABCD":
    f = f.replace(el, ' ')
print(max([len(line) for line in f.split()]))
