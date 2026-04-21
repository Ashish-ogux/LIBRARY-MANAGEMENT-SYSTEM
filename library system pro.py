
#Library Management System

books = []
issued_books = []

def add_book():
    name = input("Enter the Book Name: ")
    books.append(name)
    print(name, "is added")

def show_book():
    if len(books) == 0:
        print("No Books Available")
    else:
        print("----Avaliable Books----")
        for book in books:
            print(book)

def issue_book():
    if len(books) == 0:
        print("No books avaliable")
    else:
        show_book()
        name = input("Enter the book name: ")
        if name in books:
            books.remove(name)
            issued_books.append(name)
            print(name,"book Issued")
        else:
            print(name,"is not avaliable")

def return_book():
    name = input("Enter book name you want to return: ")
    if name in issued_books:
        issued_books.remove(name)
        books.append(name)
        print(name,"book returned")
    else:
        print(name,"Book was not issued")

def library():
    while True:
        print('\n ----MENU----')
        print('1. Add Book')
        print('2. Show Books')
        print('3. Issue Book')
        print('4. Return Book')
        print('5. Exit')

        choice = int(input("\n Enter your Choice: "))
        if choice == 1:
            add_book()
        elif choice == 2:
            show_book()
        elif choice == 3:
            issue_book()
        elif choice == 4:
            return_book()
        elif choice == 5:
            print("Thank You!")
            break
        else:
            print("Invalid Choice")

library()    
