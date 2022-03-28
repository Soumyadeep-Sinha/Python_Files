print("Program to find the palindrome number of the given number")
print()
x = int(input("ENTER THE NUMBER : "))
rev = 0
y = str(x)
while(x > 0):
    remainder = x % 10
    rev = (rev*10) + remainder
    x = x // 10
revese_num = str(rev)
new_reverse_num = revese_num[1:]
joined = y + new_reverse_num
print("PALINDROME NUMBER OF THE NUMBER IS : ", joined)