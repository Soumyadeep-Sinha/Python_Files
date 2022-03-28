print("Program to find given number is Armstrong or not.")
print()
n = int(input("ENTER THE NUMBER : "))
length = len(str(n))
sum = 0
temp = n
while(n > 0):
    r = n % 10
    sum = sum + (r**length)
    n = n // 10

if (temp == sum):
    print("IT IS AN ARMSTRONG NUMBER")
else:
    print("IT IS NOT AN ARMSTRONG NUMBER")
    
