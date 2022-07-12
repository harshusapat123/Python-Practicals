#program to find all tuples which are divisible by k

list1= [(10,14,68),(71,92,26),(45,90,135),(63,54,9)]
print("Given  tuple list:",list1)

k = int(input("Enter value of k :"))

list2 = [sub for sub in list1 if all (ele % k ==0 for ele in sub)]
print("Tuple which are divisible by k :", list2)
