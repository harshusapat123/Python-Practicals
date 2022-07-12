# program to check if the given number is a Disarium Number

def find_length(n):   #To find length of given number
    length = 0
    while (n != 0):
        length = length +1
        n = n //10
    return length

print("Enter any number :")
num =int(input())
rem =0
val =0
len = find_length(num)

n = num

while(num>0):      #calculates the sum of squares of digits
    rem = num%10
    val = val + (rem**len)
    num = num//10
    len = len -1

if (val == n):
    print(n, "is disarium number")
else:
    print(n, "is not disarium number")
    
