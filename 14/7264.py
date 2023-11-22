def convert(n):   
  res = []   
  while n:     
    res.append(n % 7)    
    n //= 7  
  return res[::-1] 
  
number = (343**515 - 6 * 49**520 + 5 * 49**510 - 3 * 7**530 - 550)
n = convert(number)
print(n.count(6))
