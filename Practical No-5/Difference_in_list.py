
#program to compute difference between two lists

def Difference(list1,list2):
    out =[]
    for i in list1:
        if not i in list2:
            out.append(i)
    return out

list1 =[11,16,21,26,31,36,41]
list2 = [26,41,36,15,78]

print("Difference between list1 and list2 : ")
print(Difference(list1,list2))

print("Difference between list2 and list1 : ")
print(Difference(list2,list1))
      
