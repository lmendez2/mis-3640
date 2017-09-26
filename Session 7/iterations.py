result = 0 ##variable to store the newest sum for multiplication use 1

"""for i in range(10):
   result = result + i + 2
   print('in the {}th iteration, result = {}' .format(i, result))
print(result)"""

for i in range(1,10, 2):
    result = result + i
    print(i) #print allows you to check the results start inclusive and stop not inclusive 

print(result)

for c in 'hello': ##printing in each character in the string 
    print(c)

for word in ['hey', 'yall']: ##square brackets represent the list 
    print(word)


import time
def countdown(n):
    while n > 0 : ##this tells us when to stop 
        print(n)
        time.sleep(1) ##delays the execution 
        n = n - 1
    print('heyyyyy')

"""countdown(10)"""


"""iteration = 0

while iteration < 5:
    count = 0 ## here each iteration it is reset to 0 
    # the variable 'letter' in the loop stands for every 
    # character, including spaces and commas!
    for letter in "hello, world": 
        count += 1
    print("Iteration " + str(iteration) + "; count is: " + str(count))
    iteration += 1 """


iteration = 0
while iteration < 5:
    count = 0
    for letter in "hello, world":
        count += 1
        if iteration % 2 == 0:
            break ##iterations 1 and 2 never break the for loop and return 12
    print("Iteration " + str(iteration) + "; count is: " + str(count))
    iteration += 1 

"""while True: ##goose for asking a user to guess a number or word 
    line = input('> ')
    if line == 'done':
        break
    print(line)
"""
print('Done!')           

mysum = 0
for i in range(5, 11, 2):
    mysum += i
    if mysum == 5:  ## when mysum  = 5 it breaks if it adds 
        break
print(mysum)