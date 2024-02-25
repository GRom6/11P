Line = open('24_2419.txt').read().strip().replace('A', 'B').split('B')
print(max(map(len, Line)))