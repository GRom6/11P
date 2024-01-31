Line = open('24_1205.txt').read().strip()
for Ch in "GWP":
    Line = Line.replace(Ch, " ")
print(max(len(x) for x in Line.split()))