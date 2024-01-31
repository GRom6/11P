from random import randint

def Is_Ip(MayIp):
    try:
        AllNum = list(map(int, MayIp.split(".")))
    except:
        return(False)

    if len(AllNum) == 4 and all(map(lambda x: x >= 0 and x < 256, AllNum)):
        return True
    else:
        return False

def CurrIs_ip():
    Str = ""
    Variation = list(map(str, range(-10, 300)))
    Variation.extend(["w", "Q", "A", "B", "C"])
    AllNum = [num for num in Variation]
    for x in range(randint(0, 6)):
        Str += str(AllNum[randint(0, len(AllNum) - 1)]) + '' * randint(0, 2) + '.'
    Str = Str[0:len(Str) - 1]
    return ("При Ip:" + "{: >25s} ".format(Str) + f"ответ был {Is_Ip(Str)}")

Answ = CurrIs_ip()
while Answ.split()[-1] != "True":
    Answ = CurrIs_ip()
    print(Answ)