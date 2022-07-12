#program to find sum of tuple elements

tuple1 = (2,5,1,9,3)
n = len(tuple1)
val =0
for i in range(0,n):
    val = val +tuple1[i]
print("Tuple :",tuple1)
print("sum of tuple elements :",val)
