print("program that prints absolute value, square root, and cube of a number.")
print()
n = float(input("ENTER A NUMBER : "))
print("ABSOLUTE VALUE OF THE NUMBER IS : ", abs(n))
if(n < 0):
    print("SQUARE ROOT OF NEGATIVE NUMBER IS NOT REAL 1")
else:
    print("SQUARE ROOT OF THE NUMBER IS : ", (n**0.5))
print("CUBE OF THE NUMBER IS : ", (n**3))