cats = ["jimmy", "Mouse", "mittens", "Oreo", "tigger"]


print('jimmy' in cats)

for cat in cats:
    print(cat)

numbers = [2, 0, 1, 6, 9]
for i in range(len(numbers)): 
    numbers[i] = numbers[i] * 2

print(numbers)


nested_list = ['spam', 1, ['New England Patriots', \
                       'Buffalo Bills', 'Miami Dolphins', \
                       'New York Giants'], \
           [1, 2, 3]]
print(len(nested_list))

a = [1 , 2 , 3]
b = [4, 5, 6]
c = a + b 
print(c)

zero_list = [0]

print(zero_list *3)

##slicing 
dogs = ["lucky", "shadow", "moose", "fluff", "floof"]
dogs.append("pup")
print(dogs)
dogs.extend("moosey")
print(dogs)

def capitalize_all(t):
    res = []
    for s in t:
        res.append(s.capitalize())
    return res

print(capitalize_all("cat"))

t = [1 , 2 , 3 ]
print(sum(t))

def only_upper(t):
    res = []
    for s in t:
        if s.isupper():
            res.append(s)
    return res
print(only_upper("cat"))
#this returns empty because nothing is upper

# t = ['a', 'b', 'c', 'd']
# x = t.pop(1)
# # pop modifies the list and returns 
# # the element that was removed. 
# print(x)
# print(t)

# x = t.pop()
# # If you don’t provide an index, 
# # it deletes and returns the last element.
# print(x)
# print(t)

# t = ['a', 'b', 'c', 'd', 'e']
# del t[1:3]
# print(t)

t = ['a', 'b', 'c']
t.remove('b')
print(t)

team = 'Patriots'
t = list(team)
print(t)

team = 'New England Patriots'
t = team.split()
print(t)

s = 'spam-spam-spam'
delimiter = '-'
t = s.split(delimiter)
print(t)

t = ['New', 'England', 'Patriots']
team = ' '.join(t)
print(team)

a = [1, 2, 3]
b = a
b is a

b[0] = 'something else'
print(a)

t = [3, 1, 2]
t2 = t[:]
t2.sort()
print(t)
print(t2)

t = [1,2,3]
x = [4]
t.append(x)
print(t)