print("program to find a maximum and minimum number out of three numbers")
print()

a = []
n = 3
for i in range(0,n) :
    num = int(input("ENTER NUMBER (%d): " %(i+1)))
    a.append(num)

a.sort()
print("MAXIMUM NUMBER IS : ",end=' ')
print(a[-1])
print("MINIMUM NUMBER IS : ",end=' ')
print(a[0])

