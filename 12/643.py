strr = '7' * 170
while "777" in strr:
    strr = strr.replace("77", '2', 1)
    strr = strr.replace("22", '7', 1)
print(strr)
