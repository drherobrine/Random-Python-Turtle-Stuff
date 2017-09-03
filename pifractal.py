import turtle

currCycle = "in"
pi = 3.1415926535
movDistance = 1
p = turtle.Pen()

while True:
    if currCycle == "in":
        movDistance *= pi
        p.forward(movDistance)
        p.left(movDistance * pi)
        currCycle = "out"
        continue
    if currCycle == "out":
        movDistance -= pi
        p.forward(movDistance)
        p.right(movDistance / pi)
        currCycle = "in"
        continue
