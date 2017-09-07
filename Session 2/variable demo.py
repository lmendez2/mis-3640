print('hello, world')

print("hey", "jude" , "don\'t make it bad")

print("46 + 37 + 38 =", 46+37+38)


"""
print('enter your name:')
username = input()
print(username)

message = 'i learned something cool!~'
"""

 
pi = 3.14


n = 100
print(n + 100)

first_name = 'lauren'
last_name = 'mendez'

fullname = first_name + " " + last_name
print(fullname)

print('hello', '%s' % 'world')
  

print('today is %2d-%02d.' % (9,5))
print('pi equals %.2f' % 3.1415926)
print('age: %s. Gender %s' % (20, True))
print('growth rate: %d %%' % 7)

minutes = 45 # current time 

# compute the percentage of the hour that has elapsed 
percentage = (minutes * 100) / 60

print(percentage)



#exercise 1.1
r = 5 #given radius 
volume = ((4/3) * pi * (r**3) ) #volume of a sphere with radius r 
print('the volume of a sphere with radius 5 is', volume)


#exercise 1.2
total = 60 # number of books calculating wholesale cost for
cover = 24.95 #original cost of book
discount = cover * (1-.40) #price of book after discount 
books = total * discount #cost of 60 books 
one = 3 #cost of shipping first book 
ads = .75 * (total - 1)
ship = one + ads #total shipping for books
cost = ('%s %.2f' % ('$',books + ship))
print('it costs ', cost , 'for 60 books')


#exercise 1.3
time = ('%d:%2d %s' % (6,52,'am')) #time left house
print('the time now is', time)
easy = ((8 *60 )+15) #time in seconds it takes for an easy lap (8 minutes * 60 seconds +15 seconds)
tempo = ((7*60)+12) # time in seconds it takes to run a lap at tempo (7 minutes * 60 seconds + 12 seconds)
run_time = (easy + (tempo*3)) #time in seconds the entire run takes 
seconds_remain = run_time%60 #this is the remainder of when run_time is divided by sixty (the seconds in a minute), in other words the seconds remaining after the the amount of minute
minutes_ran = ((run_time - seconds_remain) /60 ) # this is the number of minutes ran
total_ran = ('%2d:%2d' % (minutes_ran, seconds_remain))
print('i ran for' , total_ran)
add_minutes = ((52 + 29)%60) #number of minutes remaining after hour is completed (i.e after eight minutes has passed and it is now 7)
print('i will arrive to breakfast at' , '%d:%2d:%2d' % (6 + 1 , add_minutes , seconds_remain ), 'AM')



#exercise 1.4
before = 82
now = 89 
percent_increase = ((now - before )/ before) #change in a avg
decimal = (percent_increase * 100)
print( '%.1f %%'% (decimal)) #formating result