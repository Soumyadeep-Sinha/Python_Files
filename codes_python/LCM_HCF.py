print("Program to write the LCM and HCF of the given numbers.")
print()
#function to find lcm
def find_lcm(num1, num2):
    if(num1>num2):
        num = num1
        den = num2
    else:
        num = num2
        den = num1
    rem = num % den
    while(rem != 0):
        num = den
        den = rem
        rem = num % den
    hcf = den
    lcm = int(int(num1 * num2)/int(hcf))
    return lcm

#function to find hcf
def find_hcf(num1, num2):
    while(num2):
        num1, num2 = num2, num1 % num2
  
    return num1


a = []
n = int(input("HOW MANY NUMBERS YOU WANT TO ENTER : "))
print("ENTER THE NUMBERS => ")
for i in range(0,n) :
    x = int(input("ENTER NUMBER (%d): " %(i+1)))
    a.append(x)
 
num1 = a[0]
num2 = a[1]

lcm = find_lcm(num1, num2)
hcf = find_hcf(num1,num2)
for i in range(2, len(a)):
    lcm = find_lcm(lcm, a[i])
    hcf = find_hcf(hcf,a[i])

      
print("LCM IS : ", lcm)
print("HCF IS : ", hcf)


