print("program to enter a binary number and convert it into decimal by using loop.")
print()
num = int(input("ENTER A BINARY NUMBER : "))
dec_num = 0
base = 1

temp = num
while(temp):
    last_dig = temp % 10
    temp = int (temp / 10)
    dec_num = dec_num + (last_dig * base)
    base = base * 2

print("DECIMAL NUMBER IS : ", dec_num)