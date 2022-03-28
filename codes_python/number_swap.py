print("Program to swap two numbers without using third variable : ")
print()

a = input("ENTER FIRST NUMBER a = ")
b = input("ENTER SECOND NUMBER b = ")
print("BEFORE SWAPPING")
print("a = ", end=' ')
print(a)
print("b = ", end=' ')
print(b)

a, b = b, a

print("AFTER SWAPPING")
print("a = ", end=' ')
print(a)
print("b = ", end=' ')
print(b)