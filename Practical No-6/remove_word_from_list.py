#program to remove the ith occurrence of given word in list where word repeats
list=[]
n = int(input("Enter number of elements of list:"))
print("Enter elements of list :")
for i in range(0,n):
    element = input()
    list.append(element)
print("Given list : " ,list)
list2=[]
count =0
str = input("Enter word to remove:")
o = int(input("Enter the occurrence to remove :"))
for i in list:
        if( i == str):
            count=count+1
            if (count!=o):
                list2.append(i)
        else:
            list2.append(i)
if (count == 0):
    print("Item not found")
else:
    print("The number of repetation of ",str,"is :",count)
    print("Updated list is :", list2)
    
    
