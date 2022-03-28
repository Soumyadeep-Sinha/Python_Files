print("Program to find the reverse number of the given number")
print()
x = int(input("ENTER THE NUMBER : "))
rev = 0

while(x > 0):
    remainder = x % 10
    rev = (rev*10) + remainder
    x = x // 10

print(rev)