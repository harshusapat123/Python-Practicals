#write telephone directory of 10 students using dictionary and perform operation
#A)Finding value- key:value
#B) replacing value - key:new value
#C) replacing key value - delete key and insert key
def star():
  
    for i in range(0,60):
        print("*",end=" ")
    print("\n")
telephone_dict = { 'tanvi': 9112974690  , 'sheetal': 9326213813 ,'aarti' :9112799815 , 'gauri':8767507778 , 'akanksha': 8856919915 , 'ankita': 9067358295 , 'aniket': 7248990806, 'sanjay': 9420644874,
                                'prajackta': 8237677828 , 'omkar': 9860558121}

print("Telephone Dictionary :")
print(telephone_dict)
#A)Finding value- key:value

key=str(input("Enter key to find value:"))
print("Telephone number of given key " +key +" : ")
for i in telephone_dict.keys() :
      if  i==key:
            print(telephone_dict[i])
star()
#B) replacing value - key:new value

key=str(input("Enter key to find value:"))
value =str(input("Enter new value : "))

for i in telephone_dict.keys():
      if(i==key):
          telephone_dict[i]=value
print("Dictionary after replacement :")
print(telephone_dict)
star()
#C) replacing key value - delete key and insert key
num = int(input("Enter telephone number :"))
name =  str(input("Enter new key name :"))
old_key =0
for key,value in telephone_dict.items():
    if num==value:
        old_key = key
telephone_dict[name] = telephone_dict.pop(old_key)

print("Dictionary after replacing key:value :")
print(telephone_dict)
