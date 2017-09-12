def print_lyrics(): # after def is the name of the function 
    print("hey jude. Dont make it bad.") ## everything after the function should be indented 
    print("take a sad song and make it better")

"""print_lyrics() #callig the function we just defined

print(type(print_lyrics))  #prints the type of the def"""


def repeat_lyrics():
    print_lyrics() #calls this first
    print('na na na na na') #second
    print_lyrics() #calls again

repeat_lyrics()

def print_twice(name):
    print(name)
    print(name)

print_twice('lauren') #calls the function with one argument so lauren takes place of name 

my_name = 'lauren'
print_twice(my_name) #runs this function with varaible my_name

def my_abs(number):
    print(abs(number))


abs_number = -100
my_abs(abs_number)

def give_me_a_break():
    str1 = 'break'
    return str1
    print('another break')

print(give_me_a_break())


import math
"""def move(x, y, step, angle):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

x, y = move(100, 100, 60, math.pi /6)
print(x,y)"""


##exercise
def quadratic(a, b, c):
   xp = (-b + (math.sqrt((b**2)-(4*a*c)))) / (2 * a)
   xm = (-b - (math.sqrt((b**2)-(4*a*c)))) / (2 * a)
   print(xp , xm)


quadratic(1, -2, -8)



