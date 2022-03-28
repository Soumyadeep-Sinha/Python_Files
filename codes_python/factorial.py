print("Program to find factorial of a number")
print()
x = int(input("ENTER A NUMBER : "))
f = 1
if x < 0:
    print("Cannot calculate factorial of negative number.")
elif x == 0:
    print("FACTORIAL = 0")
else :
    for i in range(1, x + 1):
        f = f*i

print("THE FACTORIAL OF", x, "=", f)