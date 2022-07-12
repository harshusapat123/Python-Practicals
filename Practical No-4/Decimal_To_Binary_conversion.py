
#program for decimal to binary conversion

num = int(input("Enter Decimal number :"))
i =0
bnum = []
while num >0:  
    rem = num % 2
    bnum.append(rem)   #storing remainder value in arrray
    i = i+1
    num = int(num/2)

size = len(bnum)
print("Eqivalent Binary value is :",end =" ")
for  i in range(size-1, -1 ,-1):    #printing array in reverse order
    print(bnum[i], end=" ")
    
 
