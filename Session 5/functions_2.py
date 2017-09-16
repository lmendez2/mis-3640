def print_twice(whatever):
    print(whatever)
    print(whatever)


def cat_twice(part1,part2):
    cat = part1 + part2 ##local variable, only exists within the function 
    print_twice(cat)

line1 = 'Bing tiddle '
line2 = 'tiddle bang.'
cat_twice(line1, line2)

def give_me_a_break():
    str1 = "break"
    return str1 # return is the ending point of the function, whats after will not be executed it will return break at the end of the function 
    print('another break')

print(give_me_a_break()) ##give me a break is a variable 


def my_abs(n):
    if isinstance(n, int) or isinstance(n, float):    ## if n is not an integer or n is not a float 
        if n>=0:
            return n
        else:
            return -n
    else:
        print('invalid value')

print(my_abs(100))
print(my_abs(0))
print(my_abs(-4))
print(my_abs("a"))



