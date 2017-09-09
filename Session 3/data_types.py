"""age = int(input("please enter your age:"))


if age  > 21:
    print('yes, you can.')

else: 
    print('no, youre not allowed')"""

import time
print(time.time()) # seconds since epoch



seconds_remain = (int(time.time()))%60 #these are the number of seconds remaining after whole minutes are found
"""print(seconds_remain)"""
minutes = (((int(time.time())) - seconds_remain ) / 60 ) # gives us the number of minutes
"""print(minutes)"""
minutes_remain = minutes%60 #gives us the remainder amount of minutes after whole hours are found
"""print(minutes_remain)"""
hour = (minutes - minutes_remain) / 60 # gives the number of hours 
"""print(hour)""" 
hours_remain = hour%24 #gives us the remainder amount of hours after whole days are found
print(hours_remain)

current_time = ('%2d:%02d:%02d' % (hours_remain,minutes_remain,seconds_remain))
print('it is now', current_time)

print('it has been', hour, 'hours', minutes_remain, 'minutes', 'and', seconds_remain , 'seconds since epoch' )