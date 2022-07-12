#program to count occurence of each word in a given sentence

string = str(input ("Enter any sentence :"))

arr =[]
arr= string.split(" ")

count=0

print("Given sentence is :")
print(string) 
print("occurence of each word :")
i=0
while(i< len(arr)):
    count=0
    for j in arr:
        if arr[i] == j:
            count = count+1
    print(arr[i] ," :" ,count)
    i=i+1
    


