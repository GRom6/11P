def Redactor(strr):
    count = 0
    while '7777' in strr or '1111' in strr:
        if '7777' in strr:
            strr = strr.replace('7777', '1', 1)
        else:
            strr = strr.replace('1111', '7', 1)
        count += 1
    return count


strr = '7' * 512
print(Redactor(strr))
