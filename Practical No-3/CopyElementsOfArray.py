#program to copy all elements of one array to another
array1=[]
size = int (input("Enter size of array : "))
print("Enter elements of array:")
for i in range (size):
    var=int(input(  ))
    array1.append(var)
    
array2 = [None]*len(array1)   #Create second array with size of array 1

#copying all elements one array into another

for i in range(0,size):
    array2[i] = array1[i]

print("Elements of  array1(original array) :")
for i in array1:
    print(i)

print("Elements of array2 (new array) :")
for i in array2:
    print(i)
