#program to find union of two lists

n = int(input("Enter number of elements of list 1 :"))
list1 =[]
print("Enter elements of list1 :")
for i in range (0,n):
    val = input()
    list1.append(val)

m = int(input("Enter number of elements of list 2 :"))
list2 =[]
print("Enter elements of list2 :")
for i in range (0,m):
    val = input()
    list2.append(val)

print("List1:",list1)
print("List2:",list2)


        
    
elements =[]
for i in list1:
    if i not in elements:
        elements.append(i)
for i in list2:
    if i not in list1:
        elements.append(i)
print("The union of two list :", elements)
