#program to find Transpose of matrix

array =[[1,2],[3,4],[5,6]]
result = [[0,0,0],[0,0,0]]
print("Original Matrix:")
for i in array:
    print (i)
for i in range (len(array)):   #iterate through rows
    for j in range(len(array[0])): #iterate through columns
        result[j][i]= array[i][j]
print("Transpose of given matrix:")
for r in result:
    print(r)
        
