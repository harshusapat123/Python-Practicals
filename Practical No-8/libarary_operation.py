#Libaray operation
#1) Issue
#2) Return
def star():
    for i in range(0,60):
        print("*",end=" ")
    
books ={ 1120 : 'Harry Potter' , 3492: 'Cinderella' , 1500 : 'Alibaba and 40 chor ' , 6217 : 'Moon Night', 4321 : 'Arebian Nights' }
Issued_book ={}
#Issuing book
key = int(input("Enter book id to issue :"))
Issue_b = books.pop(key)
Issued_book[key] = Issue_b
print("Book which is issued :")
print(Issued_book)
print("After issuing book of id " + str(key) + " dictionary is :")
print(books)

star()
#Returning book

print("After returning book of id " + str(key) + " dictionary is :")

books.update(Issued_book)
print(books)
