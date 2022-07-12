#program to find maximum and minimum element in tuple

tuple =(13,56,22,8,25,64,78)
n = len(tuple)
max = tuple[0]
min = tuple[0]
for i in range(1,n):
    if (tuple[i] > max):
        max = tuple[i]
    elif (tuple[i] < min):
        min = tuple[i]
print("Tuple :", tuple)
print ("Maximun element :",max)
print("Minimum element :",min)
    
