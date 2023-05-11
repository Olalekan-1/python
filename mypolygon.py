import turtle
import math
bob = turtle.Turtle()
# print(bob)
# bob.fd(100)
# bob.lt(90)
# bob.fd(100)

# for i in range(4):
  #  bob.fd(100)
   # bob.lt(90)
# turtle.mainloop()




# k = turtle.Turtle()
# print(k)
# k.bk(100)
# k.lt(90)
# k.fd(100)
# k.rt(90)
# k.fd(100)
# k.rt(90)
# k.fd(100)
# turtle.mainloop()

def square(t, length):
    t = turtle.Turtle()
    for i in range(4):
        t.fd(length)
        t.lt(90)
    turtle.mainloop()




# square(bob, 320)

def polygon(t, length, n):
#    t = turtle.Turtle()
    k = 360/n
    for i in range(n):
        t.fd(length)
        t.lt(k)
   ### turtle.mainloop()

# polygon(bob, 80, 3)

def circle(t, r):
    circum = 2 * math.pi * r
    n = int(circum / 3) + 3
    length = circum / n
    polygon(t, length, n)

# circle(bob, 35)

turtle.mainloop()

"""def arc(t, angle, r):
    length = 2 * math.pi * r * angle / 360
    n = int(length / 3) + 1
    seg = length / n
    seg_angle = angle / n
    for i in range(n):
        t.fd(seg)
        t.lt(seg_angle)"""

def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = angle / n
    for i in range(n):
        t.fd(step_length)
        t.rt(step_angle)

arc(bob, 30, 10)































