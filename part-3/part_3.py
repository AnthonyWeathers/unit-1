my_book = {
    "title": "Then Hunger Games",
    "author": "Suzanne Collins",
    "year": 2008,
    "rating": 4.32,
    "pages": 374
}

# Follow the instructions in this part of the project. Define and flesh out your function below, which should accept a dictionary as an argument when called, and return a string of the info in that book-dictionary in a user-friendly readable format.

# Code below
def description (book):
    string = "This is the book's info.\n"
    for element in book:
        if(element == 'title'):
            # string = string + getTitle(book[element]) would run but wrote the get functions in next section so can't use in this one
            string = string + f"The title is {book[element]}.\n"
        elif(element == 'author'):
            # string = string + getAuthor(book[element])
            string = string + f"The author is {book[element]}.\n"
        elif(element == 'year'):
            # string = string + getYear(book[element])
            string = string + f"The year published was {book[element]}.\n"
        elif(element == 'rating'):
            # string = string + getRating(book[element])
            string = string + f"The book rating is {book[element]}.\n"
        elif(element == 'pages'):
            # string = string + getPages(book[element])
            string = string + f"The number of pages in this book is {book[element]}."
    return string
print(description(my_book))

# Once you are finished with that function, create several more functions which return individual pieces of information from the book.

# Code below
def getTitle(title):
    return f"The title is {title}.\n"
def getAuthor(author):
    return f"The author is {author}.\n"
def getYear(year):
    return f"The year published was {year}.\n"
def getRating(rating):
    return f"The book rating is {rating}.\n"
def getPages(pages):
    return f"The number of pages in this book is {pages}.\n"

# Finally, create at least three new functions that might be useful as we expand our home library app. Perhaps thing of a way you could accept additional arguments when the function is called? Also, imagine you have a list filled with dictionaries like above.

# Code below
book2 = {
    "title": "Hunger Games",
    "author": "Suzanne Collins",
    "year": 2009,
    "rating": 4.12,
    "pages": 300
}

book3 = {
    "title": "After Hunger Games",
    "author": "Suzanne Collins",
    "year": 2011,
    "rating": 4.1,
    "pages": 354
}

book_list = [my_book, book2, book3]

# additional function 1: retreive book's info by its id from the list of books
def getBook(book_list, id):
    book = description(book_list[id]) # given id would be id of the book and index book exists at in book_list and send that dictionary of book to description function
    return book
    pass

# additional function 2: retreive all books in list (via for loop through list, printing description of book)
def getBookShelf(book_list):
    shelf = ''
    for book in book_list:
        shelf = shelf + description(book) + '\n........\n'
    return shelf

# additional function 3: search for book from list by its title
def getBookByTitle(book_list, title):
    for book in book_list:
        if(book['title'] == title):
            return description(book)
    return 'Book not found'

print('....Book by id....')
print(getBook(book_list=book_list, id=2))
print('.....All books in bookshelf....')

print(getBookShelf(book_list=book_list))

print('...... Finding book by title ........')
print(getBookByTitle(book_list=book_list, title='Hunger Games'))