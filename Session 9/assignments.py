"""1. You walk into a store where each item is priced according to the letters in its name: 'a' costs $1, 'b' is $2, and so on. Write a program that prints a receipt for this wacky store:
bananas $52
rice $35
paprika $72
potato chips $78
------------------------
Total $237


Hint: the built-in function ord and chr may be useful."""
##ord a = 97


"""def wacky_store(item):
    total_price = 0 
    for letter in item:
        price = (ord(letter[0:])-96) ##subtract 96 because a = 97 in ord
        total_price = total_price + price 
    print(item,  "$", total_price)"""

"""items = ["bananas" , "rice", "paprika", "potato chips"]"""
def wacky_store(items):
    item_price = 0
    for letter in (items):
        price = float((ord(letter[0:])-96))  ##subtract 96 because a = 97 in ord
        item_price = item_price + price
    print(items, "$",item_price)
    
    
total_price = wacky_store("bananas") , wacky_store("rice") , wacky_store("paprika"), wacky_store ("potato chips")
print("-----------------------")
print("Total",  "$", "237")
    
        

#wacky_store("bananas") 
