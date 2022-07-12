#program to print all happy numbers between 1 and 100

def HappyNum(num):
    rem =0
    sum =0
    while(num>0):      #calculates the sum of squares of digits
        rem = num%10
        sum = sum +(rem*rem)
        num = num//10
    return sum

print("Happy Numbers between 1 to 100 :")
for i in range(1,101):
    
    result =i

    while(result != 1 and result !=4):
        result = HappyNum(result)

    if (result ==1):
        print (i)
    
