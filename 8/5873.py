Chet_count = len([x for x in range(0, 42) if x % 2 == 0]) - 1
Without_01_1 = 41 * 42**2 * Chet_count**2
FirstPos = Chet_count * 42**4
LastPos = 41 * 42**3 * Chet_count
Sec_Pos = (Chet_count - 1) * Chet_count * 42**3
res = Without_01_1 + FirstPos + LastPos + Sec_Pos
print(res)


