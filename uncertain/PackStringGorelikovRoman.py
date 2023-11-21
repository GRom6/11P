# Adres = input("Write adr of file")
# Array = open(Adres).readlines()
# for i in len(Array):
#     Array[i] = Array[i][:-2]

InputDate = "22D7AC18FGD"
stac = ""
result = ""
for Symb in (list(InputDate)):
    try:
        Symb = int(Symb)
        stac += str(Symb)
    except:
        if stac == '':
            result += Symb
        else:
            result += Symb * int(stac)
            stac = ''

print(result)