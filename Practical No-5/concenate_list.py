#program to concetanate two lists 
list1 = ['a','b','c']
list2 = [1,2,3,4]

c = [x+str(y) for x in list1 for y in list2]
print("list 1 : ",list1)
print("list 2 : ",list2)
print("List after concetation :")
print(c)
         
