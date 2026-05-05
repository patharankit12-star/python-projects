# create library class and make book list and no_of_book variable and find that lenth of book list and no_of_book is same for this create method

class library1:
    book=[23,21,34,45,23,56]
    
    no_of_book=0
    for i in book:
        no_of_book = 1 + no_of_book
        
    print("no_of_book is:",no_of_book)

    print(len(book))
    
    if no_of_book == len(book):
       print(1)
    else:
       print(0)   

a=library1()

class library:
    def __init__(self):
        self.noBooks= 0
        self.books=[]

    def addBook(self,book):
        self.books.append(book)
        self.noBooks = len(self.books)
    def ShowInfo(self):
        print(f"The library has {self.noBooks} books.There are ")
        for i in self.books:
            print(i)
l1=library()
l1.addBook("book1")
l1.addBook("book2")
l1.addBook("book3")
l1.addBook("book4")
l1.addBook("book5")
l1.addBook("book6")
l1.ShowInfo()
        



