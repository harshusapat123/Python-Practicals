#program to print lagest and smallest element in array

array =[]
size = int (input("Enter size of array : "))
print("Enter elements of array:")
for i in range (size):
    var=int(input(  ))
    array.append(var)
max = min = array[0]
for i in range (0,size):
    if array[i] >max:
        max = array[i]
    if array[i] <min:
        min = array[i]
print("Largest element from array : ",max)
print("Smallest element from array : ",min)
