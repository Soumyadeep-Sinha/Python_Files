print("Program to calculate sum of number from m to n.")
print()
m = int(input("ENTER THE VALUE OF m : "))
n = int(input("ENTER THE VALUE OF n : "))
if(m>n):
    print("ERROR ! m should be less than n")
    exit()
sum = 0
print()
for i in range (m, (n+1)):
    sum += i
print("SUM FROM", m,"TO", n,"IS : ", sum)