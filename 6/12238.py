import turtle as t
from time import sleep
lenghtt = 20
t.speed(50)
for i in range(2):
    t.forward(5*lenghtt)
    t.left(90)
    t.back(13*lenghtt)
    t.left(90)

t.up()
t.back(10*lenghtt)
t.right(90)
t.forward(9*lenghtt)
t.left(90)
t.down()

for i in range(2):
    t.forward(11*lenghtt)
    t.right(90)
    t.forward(7*lenghtt)
    t.right(90)

t.up()
for x in range(-15, 20):
    for y in range(-20, 5):
        t.setpos(x*lenghtt, y*lenghtt)
        t.dot()

sleep(100)
print(6*14 + 8*12 - 10)