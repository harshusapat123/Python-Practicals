#program to sort array in ascending and descending order

def AscendingOrder(array):    #sorting array in Ascending Order
    for i in range(0,size):
        for j in range (i+1,size):
             if array[i]>array[j]:
                temp = array[i]
                array[i] = array[j]
                array[j]=temp
    return array
def DescendingOrder(array):    #sorting array in Descending Order
    for i in range(0,size):
        for j in range (i+1,size):
             if array[i]<array[j]:
                temp = array[i]
                array[i] = array[j]
                array[j]=temp
    return array
array =[]
size = int (input("Enter size of array : "))
print("Enter elements of array:")
for i in range (size):
    var=int(input(  ))
    array.append(var)

print("Elements of array sorted in Ascending order:")
print(AscendingOrder(array))

print("Elements of array sorted in Descending order:")
print(DescendingOrder(array))
