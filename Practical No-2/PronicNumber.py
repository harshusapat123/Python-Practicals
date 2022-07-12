#program to print all pronic numbers between 1 and 100

def PronicNumber(num):
    flag = False

    for i in range (1, num+1):
        if ((i*(i+1) )== num):
            flag = True
            break
    return flag

print("Pronic numbers between 1 to 100 :")

for j in range (1,101):
    if (PronicNumber(j)):
        print(j)
    
