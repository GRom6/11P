def convert(n):
  res = []
  while n:
    res.append(n % 5)
    n //= 5
  return res[::-1]

number = (7 * 5**123 + 6 * 5**111 - 5 * 25**50 + 4 * 125**30 - 3 * 5**10)
n = convert(number)
print(n.count(4))
