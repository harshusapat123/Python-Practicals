#program to count unique value inside the list

list1=['a','b','c','d','a','b','f','h']
print("Input list :", list1)

list2 = []
count =0

for i in list1 :
    if i not in list2:
        count = count +1
        list2.append(i)

print("Output list :", list2)
print("Number of unique items are :",count)
