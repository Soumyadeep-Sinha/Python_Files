print("Program using for loop to calculate average of first n natural numbers.")
print()
n = int(input("ENTER HOW MANY NATURAL NUMBERS YOU WANT TO TAKE : "))
sum = 0
for i in range(1, (n+1)):
    sum += i
print("AVERAGE OF FIRST", n,"NATURAL NUMBERS IS : ", (sum/n))