def convert(n):
  res = []
  while n:
    res.append(n%25)
    n //= 25
  return res[::-1]

number = (3 * 3125**8 + 2*625**7 - 4 * 625**6 + 3 * 125**5 - 2 * 25**4 - 2024)
n = counter(number)
print(n.count(0))
