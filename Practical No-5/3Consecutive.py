 
#Program to check if list contains 3 consecutive common numbers

size = int(input("Enter size of array :"))
list =[]
for i in range(size):
    var = int(input())
    list.append(var)
print("The  3 consecutive common numbers are :")
for i in range (size-2):
    if list[i] == list[i+1] and list[i+1] == list[i+2]:
        print(list[i])
        

           
