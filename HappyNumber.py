#program to check if the given number is Happy Number

def HappyNum(num):
    rem =0
    sum =0
    while(num>0):      #calculates the sum of squares of digits
        rem = num%10
        sum = sum +(rem*rem)
        num = num//10
    return sum

print("Enter any number :")
num = int(input())
result =num

while(result != 1 and result !=4):
    result = HappyNum(result)

if (result ==1):
    print (num , "is Happy Number")
elif(result==4):
    print (num , "is not Happy Number")
    
