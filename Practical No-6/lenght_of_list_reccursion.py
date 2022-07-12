#program to find of list using recurrsion

len =0
def length(a):
    global len
    if a:
        len = len +1
        length(a [1:])
    return len

list = [1,2,3,4,5,6]

len = length(list)

print("list :", list)
print("The length of given list is :",len)
