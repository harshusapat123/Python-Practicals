# Python Program to Swap Two Variables

a = int (input("Enter value of a: "))
b = int (input("Enter value of b: "))
print ("Given :")
print("a : {0}   b : {1}".format(a,b))
temp = a
a = b
b = temp
print ("***After Swapping Values are ***")
print("a : {0}   b : {1}".format(a,b))    
