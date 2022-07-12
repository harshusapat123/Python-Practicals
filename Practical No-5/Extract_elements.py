 
#Program to extract elements with frequency greater than k 

list1 = [4, 6, 4, 3, 3, 4, 3, 7, 8, 8]
print(" Given list : " + str(list1))
K = 2
list2 = []
for i in list1:
	
	freq = list1.count(i)
	if freq > K and i not in list2:
		list2.append(i)

print("K = ",K)
print("Elements greater than given frequency: " + str(list2))
