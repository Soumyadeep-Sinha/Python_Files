print("Program to print the multiplication table of n where n is given by user")
print()
n = int(input("ENTER THE NUMBER : "))
x = int(input("ENTER UP TO WHICH NUMBER YOU WANT TO FIND TABLE : "))
print()
print("TABLE OF n IS : ")
print()
for i in range (0, x+1):
    y = n * i
    print(n, "X", i, "=", y)
