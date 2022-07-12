#program to print elements of array in reverse order
array =[]
size = int (input("Enter size of array : "))
print("Enter elements of array:")
for i in range (size):
    var=int(input(  ))
    array.append(var)
print("Elements of given array :")
for i in range (0,size):
    print(array[i])
print("Elements of array in reverse order:")
for i in range(size-1,-1,-1):
    print(array[i])
