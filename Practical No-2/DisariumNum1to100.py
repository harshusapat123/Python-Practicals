#program to print all disarium numbers between 1 and 100

def find_length(n):   #To find length of given number
    length = 0
    while (n != 0):
        length = length +1
        n = n //10
    return length


def TotalSum(num):      # to find sum of digits of number
    rem = sum =0
    len = find_length(num)
    while (num>0):
        rem = num %10
        sum = sum +(rem **len)
        num = num//10
        len =len-1
    return sum

value =0
print("Disarium number between 1 to 100 are :")
for i in range (1 ,101):
    value = TotalSum(i)
    if (value == i):
        print(i)
    
