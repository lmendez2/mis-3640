from math import sqrt

def mysqrt(a):
    while True:
        print(x)
        y = (x + a/x) / 2
        if y == x:
            break
        x = y

print("a", "    ", "mysqrt(a)", "   ", "math.sqrt(a)", "    ", "diff")
print("-", "    ", "---------", "   ", "------------", "    ", "----" )

def test_square_root():    
    results = [(a ,mysqrt(a), sqrt(a)) for a in range(1,10)]
    print(results)



