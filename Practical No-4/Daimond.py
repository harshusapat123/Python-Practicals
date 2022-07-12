#program to Diamond

row = int(input("Enter number of rows :"))

for i in range(0, row):            # iterations for row number
    for j in range (0, row -i-1):  # iterations for printing spaces before *
        print(end =" ")
    for p in range (0,i+1):         #iterations for printing *
        print("*",end=" ")
    print()
    
for i in range(row-1, 0,-1):            
    for j in range ( row ,i,-1):
        print(end =" ")
    for p in range (0,i):         
        print("*",end=" ")
    print()
