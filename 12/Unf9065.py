def R(strr):
    while '>1' in strr or '>2' in strr or '>0' in strr:
        if '>1' in strr:
            strr = strr.replace('>1', '22>')
        if '>2' in strr:
            strr = strr.replace('>2', '2>')
        if '>0' in strr:
            strr = strr.replace('>0', '1>')

def prime(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    else:
        return True

