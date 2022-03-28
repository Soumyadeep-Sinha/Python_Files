print("Program to display Fibonacci sequence of n terms")
print()
n = int(input("ENTER THE NUMBER OF TURNS YOU WANT : "))
n1 = 0
n2 = 1
count = 0

# validity
if(n <= 0):
    print("INVALID INPUT! INPUT MUST BE POSITIVE")
elif n == 1:
    print("FIBONACCI SERIES : ", n2)
else:
    print("FIBONACCI SEQUENCE UPTO", n,"TERMS : ", end=' ')
    while count < n:
        print(n1, end=' ')
        temp = n1 + n2
        n1 = n2
        n2 = temp
        count += 1