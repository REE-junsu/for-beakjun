
import turtle as t
t.bgcolor("black")
t.hideturtle()
t.speed(0)
for x in range(1000):
    if x%5==0:
        t.color("red")
    if x%5==1:
        t.color("blue")
    if x%5==2:
        t.color("green")
    if x%5==3:
        t.color("yellow")
    if x%5==4:
        t.color("orange")
    t.fd(x*2)
    t.rt(143.5)
