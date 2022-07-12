
#program to print both number and star pattern

for i in range (1,5):                   #iteration for row numbers
    for j in range (1,i+1):           # iterations for printing numbers and stars
        if (j<i):
            print( i,"*"  , end =" ")    #print number with star(*)
        else:
            print (i)                            #print only number 
    print()

for i in range (4,0,-1):
    for j in range (1,i+1):
        if (j<i):
            print( i,"*"  , end =" ")
        else:
            print (i)
    print()

