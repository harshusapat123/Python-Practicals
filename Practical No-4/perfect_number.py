
#program to find given number is perfect number or not

num = int(input("Enter any number : "))
sum =0
for i in range (1,num):
    if ( num %  i ==0): 
        sum = sum +i
if (sum == num):
    print(num ,"is Perfect number.")
else:
    print(num, "is not Perfect number.")
    
