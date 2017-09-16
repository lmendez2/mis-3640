import turtle
import math 

jimmy = turtle.Turtle() 

print(jimmy)

"""for i in range(4): ##for loops require indentation 
    jimmy.fd(100)
    jimmy.lt(90)"""

"""jimmy.fd(100)
jimmy.lt(90)
jimmy.fd(100)
jimmy.lt(90)
jimmy.fd(100)
jimmy.lt(90)"""




def square(t,length):
    for i in range(4):
        t.fd(length)
        t.lt(90)

square(jimmy, 25)

def polygon(t,length,n):
    for i in range(n):
        t.fd(length)
        t.lt(360/n)


polygon(jimmy, 25, 5)

def circle (t, r):
    circum = 2 * math.pi * r
    n = 100
    length = circum/ n
    polygon(t, length, n) ## sequence has to match from previous 

circle(jimmy, 40)

def arc (t, r, angle):
    arc_len = 2 * math.pi * r * angle/ 360
    n = int(arc_len/3) +1
    step_length = arc_len / n
    step_angle = angle / n

    for i in range(n):
        t.fd(step_length)
        t.lt(step_angle)

arc(jimmy,100,90)
    


turtle.mainloop()