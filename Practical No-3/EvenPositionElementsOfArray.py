#program to print elements of array present on even position

array =[]
size = int (input("Enter size of array : "))
print("Enter elements of array:")
for i in range (size):
    var=int(input(  ))
    array.append(var)
print("Elements of given array :")
for i in range (0,size):
    print(array[i])
print ("Elements on even position of array:")
for i in range (1,size,2):
    print(array[i])
