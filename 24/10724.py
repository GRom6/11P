file = open('10724.py').readline().strip()

file = file.replace('T', ' ').split()
len_el = [len(line) for line in file]
print(len_el)

