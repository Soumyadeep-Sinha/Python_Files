print("Program to find the sum of numbers")
print()
n = int(input("ENTER TOTAL NUMBERS : "))
a = []
sum = 0
for i in range(0,n):
    num = int(input("ENTER NUMBER %d: " %(i+1)))
    a.append(num)
    sum = sum + a[i]
print("SUM OF THE NUMBERS = ", sum)
