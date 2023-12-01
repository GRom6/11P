def F(n, m):
     StrangeSum = str(int(n[0]) + int(m[0]))
     StrangeSum += str(int(n[1]) + int(m[1]))
     StrangeSum = str(int(n[2]) + int(m[2])) + StrangeSum

     while len(StrangeSum) < 5:
          StrangeSum = '0' + StrangeSum

     ControlS = StrangeSum[-4] + StrangeSum[-3] + StrangeSum[-2]
     print(StrangeSum, ControlS)
     return ControlS

print(F("473", "934"))

for FirsN in range(999, 99, -1):
     FirsN = str(FirsN)
     while len(FirsN) != 3:
          FirsN = '0' + FirsN

     for SecN in range(100, 1000):
          SecN = str(SecN)
          while len(SecN) != 3:
               SecN = '0' + SecN

          if F(FirsN, SecN) == '002':
               print(FirsN)
               break
     else:
          continue
     break


