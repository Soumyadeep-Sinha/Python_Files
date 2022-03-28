print("Program to find factor of a given number")
print()

n = int(input("ENTER THE NUMBER : "))
print("FACTORS ARE : ", end=' ')
for i in range(1, n+1):
    if(n % i == 0):
        print(i, end=',')

