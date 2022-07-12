#program to count tuple occurence in list of tuples

list1= [(1,2,3), ('a','b'),(10,60),(1,2,3),('a','b','c'),('a','b')]

value =[]
for i in list1:
    value.append(i)

count =0

print("Tuple :",tuple)
print("occurence of each tuple :")

i =0
while (i<len(value)):
    count =0
    for j in value :
        if value[i] == j:
            count = count+1
    print(value[i] ,":",count)
    i=i+1

