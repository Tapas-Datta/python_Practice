
library_books =['Python', 'C Programming', 'Java', 'HTML', 'SQL']
print("do you want to see the all books list, press 0")
print("do you want the books,press 1")
print("do you want remove the books,press 2")
print("do you want to search any books,press 3")
print("do you want to see the total number of books,press 4")
print("do you want stop the program,press 5")
while True:
    user_choice = int(input("enter your choice:"))
    if user_choice ==0:
        print(" the book list we have now is ",library_books)
    elif user_choice ==1:
        new_book = input("enter the book you want to add:")
        library_books.append(new_book)
        print(" the book you have now after add is ",library_books)
    elif user_choice ==2:
        new_book = input("enter the book you want to remove:")
        if new_book in library_books:
            library_books.remove(new_book)
            print(" the book you have now after remove is ",library_books)
        else:
            print("book not found")
    elif user_choice ==3:
        search_book = input("enter the book you want to search:")
        if search_book in library_books:
            print("that book is found",search_book)
        else:
            print("that book is not found")
    elif user_choice ==4:
        total = 0
        for book in library_books:
            if book in library_books:
                total+=1
        print("total number of books is :",total)
    elif user_choice ==5:
       print("good bye for your time being with us")
       break


