trans = {'0':'ling', '1':'yi', '2':'er', '3':'san', '4': 'si', '5':'wu', 
         '6':'liu', '7':'qi', '8':'ba', '9':'jiu', '10': 'shi', '100': 'bai'}


def speak_Chinese(number):
    '''
    number: an integer, 0<=number<=999

    Returns: a string that is the number in Chinese
    '''
    while number < 1000:
        # print("Hello, I can help you translate some numbers into Mandarin!")
        # number = int(input("Please input a number (0-999) to translate into Mandarin: "))
        #r1 these are the words for each of the digits from 0-10 
        if number < 11:
            r1 = str(number)
            a = trans[r1]
            return a  #returns the value a for the key r1

        #r2 for numbers 11-19 number is "ten digit" ex: 16 = ten six
        if number > 10 and number < 20:
            r2 = number - 10
            r1 = str(r2)
            b = trans[r1]
            return 'shi' + ' ' + b 
        
        #r3.a for numbers between 20 and 99 number is digit ten digit ex: 37 = three ten seven 
        #r3.b if digit is a zero it is not included and it is digit ten ex: 50 = five ten 
        if number > 19 and number < 100: 
            if number % 10 != 0:
                r3_a = str(number)
                for number in r3_a:
                    left = r3_a[0]
                    tleft = trans[left]
                    right = r3_a[-1]
                    tright = trans[right]
                    return tleft + " " + "shi" + " " + tright
            else:
                r3_b = int(number/10)
                d = str('{:d}'.format(r3_b))
                c = trans[d]
                return c + ' ' + "shi"

        #r4 number 100 is one hundred 
        if number % 100 == 0: 
            r4 = int(number/100)
            d = str('{:d}'.format(r4))
            c = trans[d]
            return c + ' ' + "bai"


        #r5 for numbers between 101 and 999 if second digit is 0 then its digit hundred zero digit
        #ex 307 is three hundred zero seven 
        if number > 100 and number < 1000: 
            r5 = str(number)
            if r5[1] == 0 and r5[-1] != 0:
                left = r5[0]
                tleft = trans[left]
                right = r5[-1]
                tright = trans[right]
                return tleft + " " + "bai" + " " + "ling" + " " + tright
        #r6.a if second digit is not zero then its digit hundred digit ten digit 
        #ex 537 is five hundred three ten seven 
        #r6.b if the last digit is a zero then its not included
        #ex 450 is four hundred five ten 
            elif r5[1] != 0 and r5[-1] != 0:
                left = r5[0]
                tleft = trans[left]
                right = r5[-1]
                tright = trans[right]
                mid = r5[1]
                tmid = trans[mid]
                return tleft + " " + "bai" + " " + tmid + " " + "shi" + " " + tright
            else: 
                left = r5[0]
                tleft = trans[left]
                mid = r5[1]
                tmid = trans[mid]
                return tleft + " " + "bai" + " " + tmid + "shi"
    # else:
    #     return "Sorry, I can't translate numbers above 999, try again"     
    ## added the while loop in case i had time to retouch it 
          
# For testing
def main():
    print(speak_Chinese(36))
    print('In Chinese: 36 = san shi liu')
    print(speak_Chinese(20))
    print('In Chinese: 20 = er shi')
    print(speak_Chinese(16))
    print('In Chinese: 16 = shi liu')
    print(speak_Chinese(200))
    print('In Chinese: 200 = er bai')
    print(speak_Chinese(109))
    print('In Chinese: 109 = yi bai ling jiu')
    print(speak_Chinese(999))
    print('In Chinese: 999 = jiu bai jiu shi jiu')
    

if __name__ == '__main__':
    main()
