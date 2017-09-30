# team = 'new england patriots'

# letter = team[-1]  #negatives go backward square brackets refer to index

# print(len(team)) 

# print(team[len(team)-1])




"""for i in range(len(team)):
    if team[i] != ' ':
        print(team[i])"""

"""for letter in team:
    if letter.isalpha(): ##will only print if letter is alphabet
        print(letter)"""


"""prefixes = 'JKLMNOPQ'
suffix = 'ack'
for letter in prefixes:
    if letter == "Q" or letter == "O": ##have to define letter again after or 
        print(letter + "u" + suffix)
    else:
        print(letter + suffix)"""

"""print(team[0:11])
print(team[12:20])
print(team[:11])
print(team[12:])
print(team[::-1]) ##prints it backwards 
print(team[::-2]) ##prints everyother backwards
print(team[::1])
print(team[::2]) ##prints every other forwards """


team = 'new england patriots'
# team[12:20] = 'seahawks'

print(team)

new_team = team[:12] + "beavers"
print(new_team)

def find(word, letter):
    index = 0
    while index < len(word):
        if word[index] == letter:
            return index
        index = index + 1
    return -1

print(find(team, 'W'))

# word = 'New England Patriots'   ##this counts the number of 'a's in the word
# count = 0
# for letter in word:
#     if letter == 'a':
#         count = count + 1
# print(count)

def count(word, letter):
    c = 0 
    for x in word:
        if x == letter:
            c = c + 1
    return c 



number_of_vowels = count(team, "a") + count(team, "e") + count(team, "i") + count(team, "o") + count(team, "u")
print(number_of_vowels)

vowels = 'aeiou'
number_of_vowels = 0
for letter in vowels:
    number_of_vowels += count(team, letter)

print(number_of_vowels) 

def low(word, letter):
    lower = word.lower()
    c = 0 
    for x in lower:
        if x == letter.lower():
            c = c +1 
    return c

print(low("caAaat", "a"))

def in_both(word1, word2):
    for letter in word1:
        if letter in word2:
            print(letter)