"""age=input("what is your age?")
age=int(age)


if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')"""

import time

def countdown(n):
    if n <= 0:
        print('Blastoff!')
    else:
        print(n)
        time.sleep(2)
        countdown(n-1)

countdown(5)

def print_s(s , n):
    if n <= 0:
        return
    print(s)
    print_n(s, n-1)