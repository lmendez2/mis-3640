import random 
import turtle
drunk = turtle.Turtle()
print(drunk)
drunk.pendown()


def drunkard_walk(x, y, n):
    """
    The Drunkard’s Walk. A drunkard in a grid of streets randomly picks one of four directions and stumbles to the next intersection, then again randomly picks one of four directions, and so on. You might think that on average the drunkard doesn’t move very far because the choices cancel each other out, but that is actually not the case.

	Write a function to calculate the distance after n intersections.

    x, y: the original location
    n: the number of intersections(steps)
    return the distance after n intersections(steps) from the origin
    """
    x = 0       #the origin
    y = 0
    x_walk = '' #later used to state the position of the drunk
    y_walk = ''
    for i in range(n):
        directon = random.randint(0,4) #helps us choose a random direction for the drunk
        if direction == 0: #when 0 it will turn 90 
            x = x + 1
            y = y + 0
            print("the drunk walks right")
            drunk.setheading(90)
        elif direction == 1: #when one it will not turn 
            y = y + 1
            x = x + 0
            print("the drunk walks forward")
            drunk.setheading(0)
        elif direction == 2: #when 2 it will turn left
            x = x - 1
            y = y + 0
            print("the drunk walks left")
            drunk.setheading(270)
        else:               #finally when 3 it will turn around
            y = y - 1
            x = x + 0
            print("the drunk walks backward")
            drunk.setheading(180)
        drunk.fd(10)
    
    if x >= 0:
        x_walk = "right"
    else:
        x_walk = "left"
    if y >= 0: 
        y_walk = "forward"
    else:
        y_walk = "backward"
        



    distance = (x_walk, x, "and", y_walk, y)
    print("The drunkard started from (%d,%d)." % (x, y))
    print("After", n , "intersections, he's", distance, "blocks from where he started.")


drunkard_walk(0,0,2)

turtle.mainloop()
