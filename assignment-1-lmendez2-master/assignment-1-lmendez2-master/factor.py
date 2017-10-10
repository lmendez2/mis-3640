n = int(input("please enter an integer to find its prime factors"))
#have to convert the string into an integer


def factor(n):
    """
    Factoring of integers. Write a program that asks the user for an integer and then prints out all its factors. 
    For example, when the user enters 150, the program should print 2 3 5 5
    """
    ##searching for prime factorization not just factors!!###
    prime_factors = [] ## here is where we will store our prime factors as the code finds it 
    d = 2 # the lowest possible prime number,
    while n > 1:
        if n % d == 0: 
            prime_factors.append(d) #we append as many 2's needed as we divide n by 2 
            n = n/d #we repeat the process of dividing n by two as long as the remainder is 0
        else: 
            d = d + 1 #when n%d != 0 we reset d 
    return(prime_factors)

print(factor(n))


    

