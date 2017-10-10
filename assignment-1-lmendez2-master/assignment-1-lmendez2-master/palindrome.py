s = input("Enter a string: ")

def isPalindrome(s):
    """
    Write a recursive function isPalindrome(string) that returns True if string is a palindrome, 
    that is, a word that is the same when reversed. Examples of palindromes are “deed”, “rotor”, or “aibohphobia”. 
    Hint: A word is a palindrome if the frst and last letters match and the remainder is also a palindrome.
    """
    if len(s) < 2: #if the length of the string is less than 2 (1) then the function should return true since one letter is a palindrome
        return True
    elif s[0] == s[-1]: #else if the length of the string is greater than 1 and the first and last letter of the string are the same the a recursion call occurs with the first and last letters sliced until the base case it met or the letters dont match
        return isPalindrome(s[1:-1])
    else:
        return False

if (isPalindrome(s) == True):  #according to the function above, when isPalindrome returns true, print "that's a palindrome"
    print("That's a palindrome.")
else:                       #according to the function above, when isPalindrome returns false, print "that's not palindrome"
    print("That's not palindrome.")


isPalindrome(s)


# print(isPalindrome("rotor")) #true
# print(isPalindrome("cat")) #false
# print(isPalindrome("deed")) #true
# print(isPalindrome("bob")) #true
# print(isPalindrome("aibohphobia")) #true