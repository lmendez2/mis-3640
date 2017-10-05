# fin = open('words.txt')
# line = fin.readline()
# print(repr(line))


# def find_long_words():
#     fin = open('words.txt')
#     for line in fin:
#         word = line.strip()
#         if len(word) > 20:
#             print(word)

#find_long_words()

def has_no_e(word):
    for letter in word:
        if letter.lower() == 'e':
            return False
    return True 

    """return not 'e' in word.lower()"""  ### this gets it done in one line

print(has_no_e("cat"))
print(has_no_e("babson"))
print(has_no_e("eat"))

def fine_words_no_e():
    fin = open('words.txt')
    total_count = 0
    no_e = 0
    for line in fin:
        word = line.strip()
        total_count = total_count + 1
        if has_no_e(word):
            # print(word)
            no_e= no_e + 1
    return no_e/total_count
    


#print('the percentage of the words with no '"e"' is {:.2}%.'.format(fine_words_no_e()*100))

def avoids(word, forbidden):
    for letter in word:
        if letter in forbidden:
            return False
    return True

print(avoids("babson", "z"))
print(avoids("college", "z"))

def fine_words_no_vowel():
    fin = open('words.txt')
    total_count = 0
    no_v = 0
    for line in fin:
        word = line.strip()
        total_count = total_count + 1
        if avoids(word , "aeiouy"):
            print(word)
            no_v= no_v + 1
    return no_v/total_count

#print('the percentage of the words with no '"aeuioy"' is {:.2}%.'.format(fine_words_no_vowel()*100))

##takes a word and string of letters returns true if the word contains only letter in the list
def uses_only(word, available):
    for letter in word: 
        if letter not in available:
            return False
    return True
print(uses_only("cat","at"))
print(uses_only("cat", "bc"))

##takes a word and string of letters and returns true if the word uses all the required letters at least once
def uses_all(word, required):
    for letter in required: 
        if letter not in word:
            return False
    return True
print(uses_all("cat","bat"))
print(uses_all("back","ck"))


##returns True if the letter appear in alphabetical order. Double letters are okay
def is_abecedarian(word):
    previous = word[0]
    for c in word:
        if c < previous:
            return False
        previous = c
    return True

print(is_abecedarian("tear"))
print(is_abecedarian("abs"))

def is_abecedarian_while(word):
    previous = word[0]
    while ord(previous) < ord(previous +1):
        return True
    return False
print(is_abecedarian_while("abs"))

def is_abecedarian_rec(word):
    previous = word[0]
    for letter in word:
        if chr(previous) < chr(previous +1):
            return True
    return False
print(is_abecedarian_while("abs"))