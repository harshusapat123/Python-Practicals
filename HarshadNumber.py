#program to determine whether the given number is a Harshad Number

print("Enter any number :")
num = int(input())
rem =0
sum =0

val = num

while (num >0):    #calculates sum of digits
    rem = num%10
    sum = sum +rem
    num = num //10

if (val % sum ==0):
    print(val , "is Harshad Number.")
else:
       print(val , "is not Harshad Number.")
    
