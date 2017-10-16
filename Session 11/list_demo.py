AFC_east = ['New England Patriots', 'Buffalo Bills', 'Miami Dolphins', 'New York Jets']
numbers = [42, 123]
empty = []
#print(AFC_east, numbers, empty)

AFC_east[3] = 'New York Giants'
print(AFC_east)

AFC_east[-1]
print("Buffalo Bills" in AFC_east) 

L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', ['Ruby','On Rail'], 'PHP'],
    ['Adam', 'Bart', 'Lisa']
    
]

# for team in AFC_east:
#     print(team)

numbers = [2, 0, 1, 6, 9]

for i in range(len(numbers)):   ## multiplies everything by 2
    numbers[i] = numbers[i] * 2
    
print(numbers)

my_list = ['spam', 1, ['New England Patriots', \
                       'Buffalo Bills', 'Miami Dolphins', \
                       'New York Giants'], \
           [1, 2, 3]]
print(len(my_list))


my_animals = ["jimmy", "feathers", "mouse", "blue"]
my_animals.append("scaly") 
print(my_animals)
my_animals.extend(["lucky", "shadow"])
print(my_animals)
my_animals.insert(2,"Oreo", )
print(my_animals)

#scaly and blue died 
my_animals.remove("scaly")
print(my_animals)
my_animals.remove("blue")
print(my_animals)

def only_upper(t):
    res = []
    for s in t:
        if s.isupper():
            res.append(s)
    return res

print(only_upper("babson collegE"))


def binary_search(word):
     fin = open('words.txt')
    total_count = 0
    for line in fin:
        word = line.strip()
        total_count = total_count + 1
        



