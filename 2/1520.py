for c in range(2):
  for b in range(2):
    for a in range(2):
      print(c, b, a, ((bool(a)<=bool(b)) and ((bool(a) and bool(b)) <= (not bool(c)))))