import turtle
import math

turtle.speed(0)
turtle.delay(0)

##exercise 1

tri1 = turtle.Turtle()
tri2 = turtle.Turtle()
tri3 = turtle.Turtle()
tri4 = turtle.Turtle()
big = turtle.Turtle()
l1 = turtle.Turtle()
l2 = turtle.Turtle()
l3 = turtle.Turtle()
l4 = turtle.Turtle()


l1.penup()
l1.setpos(1,13)
l2.penup()
l2.setposition(60,72)
l3.penup()
l3.setposition(-58,72)
l4.penup()
l4.setposition(1,130)


tri1.penup()
tri1.setpos(2,100)
tri1.seth(-30)


tri2.penup()
tri2.setpos(2,100)
tri2.seth(-120)

tri3.penup()
tri3.setpos(2,100)
tri3.seth(-210)

tri4.penup()
tri4.setpos(2,100)
tri4.seth(-300)



turtle.penup()
def poly(t,length,n):
    for i in range(n):
        t.fd(length)
        t.lt(360/n)


def circle (t, r):
    circum = 2 * math.pi * r
    n = 100
    length = circum/ n
    poly(t, length, n)



circle(big,100)
big.hideturtle()
l1.pendown()
circle(l1,28)
l1.hideturtle()
l2.pendown()
l2.hideturtle()
circle(l2,28)
l3.pendown()
circle(l3,28)
l3.hideturtle()
l4.pendown()
circle(l4,28)
l4.hideturtle()
tri1.pendown()
poly(tri1,100,3)
tri1.hideturtle()
tri2.pendown()
poly(tri2,100,3)
tri2.hideturtle()
tri3.pendown()
poly(tri3,100,3)
tri3.hideturtle()
tri4.pendown()
poly(tri4,100,3)
tri4.hideturtle()

##end of excercise 1
#####
#####

###excercise 2
###excercise 2
###excercise 2


thin = turtle.Turtle()
thin.penup()
thin.color("silver")
thin.setposition(0,-400)
thin.pendown()
circle(thin,100)
thin.hideturtle()

def arc (t, r, angle):
    arc_len = 2 * math.pi * r * angle/ 360
    n = int(arc_len/3) +1
    step_length = arc_len / n
    step_angle = angle / n

    for i in range(n):
        t.fd(step_length)
        t.lt(step_angle)



arc1 = turtle.Turtle()
arc1.penup()
arc1.color("silver")
arc1.setposition(0,-300)
arc1.seth(60)
arc1.pendown()
arc1.circle(100,60,None)
arc1.hideturtle()


arc1a = turtle.Turtle()
arc1a.penup()
arc1a.color("silver")
arc1a.setposition(0,-300)
arc1a.seth(-60)
arc1a.pendown()
arc1a.circle(100,-60,None)
arc1a.hideturtle()

arc2 = turtle.Turtle()
arc2.penup()
arc2.color("silver")
arc2.setposition(0,-300)
arc2.seth(120)
arc2.pendown()
arc2.circle(100,60,None)
arc2.hideturtle()

arc2a = turtle.Turtle()
arc2a.penup()
arc2a.color("silver")
arc2a.setposition(0,-300)
arc2a.seth(-120)
arc2a.pendown()
arc2a.circle(100,-60,None)
arc2a.hideturtle()

arc3 = turtle.Turtle()
arc3.penup()
arc3.color("silver")
arc3.setposition(0,-300)
arc3.seth(180)
arc3.pendown()
arc3.circle(100,60,None)
arc3.hideturtle()

arc3a = turtle.Turtle()
arc3a.penup()
arc3a.color("silver")
arc3a.setposition(0,-300)
arc3a.seth(-180)
arc3a.pendown()
arc3a.circle(100,-60,None)
arc3a.hideturtle()

arc4 = turtle.Turtle()
arc4.penup()
arc4.color("silver")
arc4.setposition(0,-300)
arc4.seth(240)
arc4.pendown()
arc4.circle(100,60,None)
arc4.hideturtle()

arc4a = turtle.Turtle()
arc4a.penup()
arc4a.color("silver")
arc4a.setposition(0,-300)
arc4a.seth(-240)
arc4a.pendown()
arc4a.circle(100,-60,None)
arc4a.hideturtle()

arc5 = turtle.Turtle()
arc5.penup()
arc5.color("silver")
arc5.setposition(0,-300)
arc5.seth(300)
arc5.pendown()
arc5.circle(100,60,None)
arc5.hideturtle()

arc5a = turtle.Turtle()
arc5a.penup()
arc5a.color("silver")
arc5a.setposition(0,-300)
arc5a.seth(-300)
arc5a.pendown()
arc5a.circle(100,-60,None)
arc5a.hideturtle()

arc6 = turtle.Turtle()
arc6.penup()
arc6.color("silver")
arc6.setposition(0,-300)
arc6.seth(360)
arc6.pendown()
arc6.circle(100,60,None)
arc6.hideturtle()

arc6a = turtle.Turtle()
arc6a.penup()
arc6a.color("silver")
arc6a.setposition(0,-300)
arc6a.seth(-360)
arc6a.pendown()
arc6a.circle(100,-60,None)
arc6a.hideturtle() 


###end of exercise 2
###end of exercise 2


## excercise 3 
## excercise 3

thick = turtle.Turtle()
thick.penup()
thick.width(4)
thick.setposition(300,-200)
thick.pendown()
circle(thick,100)
thick.hideturtle()

s1 = turtle.Turtle()
s1.penup()
s1.width(4)
s1.setposition(300,-170)
s1.pendown()
circle(s1,13)
s1.hideturtle()

s2 = turtle.Turtle()
s2.penup()
s2.width(4)
s2.setposition(300,-60)
s2.pendown()
circle(s2,13)
s2.hideturtle()

semi1 = turtle.Turtle()
semi1.penup()
semi1.setposition(300,-200)
semi1.width(4)
semi1.pendown()
semi1.circle(50,180,None)
semi1.hideturtle()

semi2 = turtle.Turtle()
semi2.penup()
semi2.setposition(300,-100)
semi2.width(4)
semi2.pendown()
semi2.circle(50,-180,None)
semi2.hideturtle()



###just for fun

lc1 = turtle.Turtle()
lc1.penup()
lc1.color("pink")
lc1.setposition(-280,-100)
lc1.pendown()
circle(lc1,10)
lc1.hideturtle()

lc2 = turtle.Turtle()
lc2.penup()
lc2.color("pink")
lc2.setposition(-320,-100)
lc2.pendown()
circle(lc2,10)
lc2.hideturtle()

bc1 = turtle.Turtle()
bc1.penup()
bc1.color("pink")
bc1.setposition(-300,-120)
bc1.pendown()
circle(bc1,40)
bc1.hideturtle()

lc1 = turtle.Turtle()
lc1.penup()
lc1.color("black")
lc1.setposition(-270,-40)
lc1.pendown()
circle(lc1,12)
lc1.hideturtle()

lc2 = turtle.Turtle()
lc2.penup()
lc2.color("black")
lc2.setposition(-330,-40)
lc2.pendown()
circle(lc2,12)
lc2.hideturtle()

bc2 = turtle.Turtle()
bc2.penup()
bc2.color("pink")
bc2.setposition(-300,-180)
bc2.pendown()
circle(bc2,100)
bc2.hideturtle()

e1 = turtle.Turtle()
e1.penup()
e1.setposition(-220, -18)
e1.color("pink")
e1.pendown()
e1.circle(25,270,None)
e1.hideturtle()

bc3 = turtle.Turtle()
bc3.penup()
bc3.color("pink")
bc3.setposition(-300,-240)
bc3.pendown()
circle(bc3,150)
bc3.hideturtle()

e2 = turtle.Turtle()
e2.penup()
e2.setposition(-375, -18)
e2.color("pink")
e2.pendown()
e2.circle(25,-270,None)
e2.hideturtle()

turtle.mainloop()