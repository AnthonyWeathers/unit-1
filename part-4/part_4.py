### Step 1 - Input function

## Create five input statements to gather user's book they want to input to the system. After that be sure to turn it into a function.

# Code here
# def create_new_book():
#    print('Fill out the information to add your book.')
#    title = input("Title: ")
#    author = input("Author: ")
#    year = input("Year published: ")
#    rating = input("Rating: ")
#    pages = input("# of pages: ")

#    book_dictionary = {
#       "title": title,
#       "author": author,
#       "year": year,
#       "rating": rating,
#       "pages": pages
#    }

#    return book_dictionary

# book = create_new_book()
# print(book)

### Step 2 - Type conversion

## Now convert the proper data-types front strings to either floats or ints depending on what it is. Feel free to comment out your old function so you don't get an error, or copy/paste and give it a new name.

# Code here
# def create_new_book():
#    print('Fill out the information to add your book.')
#    title = input("Title: ")
#    author = input("Author: ")
#    year = int(input("Year published: "))
#    rating = float(input("Rating: "))
#    pages = int(input("# of pages: "))

#    book_dictionary = {
#       "title": title,
#       "author": author,
#       "year": year,
#       "rating": rating,
#       "pages": pages
#    }
#    print(type(book_dictionary['year']))
#    print(type(book_dictionary['rating']))
#    print(type(book_dictionary['pages']))

#    return book_dictionary
# book = create_new_book()
# print(book)

### Step 3 - Error handling

## Now take your previous function, and handle potential errors should the user type an answer that doesn't convert data-type properly.

# Code here
# def create_new_book():
#     print('Fill out the information to add your book.')
#     title = input("Title: ")
#     author = input("Author: ")
#     # year = int(input("Year published: "))
#     try:
#         year = int(input("Year published: "))
#     except:
#         year = int(input("Please enter a number for the year published: "))
#     # rating = float(input("Rating: "))
#     try:
#         rating = float(input("Rating: "))
#     except:
#         rating = float(input("Please enter a number for the rating: "))
#     # pages = int(input("# of pages: "))
#     try:
#         pages = int(input("# of pages: "))
#     except:
#         pages = int(input("Please enter a number for the number of pages: "))


#     book_dictionary = {
#       "title": title,
#       "author": author,
#       "year": year,
#       "rating": rating,
#       "pages": pages
#     }
#     print(type(book_dictionary['year']))
#     print(type(book_dictionary['rating']))
#     print(type(book_dictionary['pages']))

#     return book_dictionary
# book = create_new_book()
# print(book)


### Step 4 - if/elif/else

## Now create a main menu function that gives the user options. Handle their choices with if/elif/else statements.

# Code here
# my_book = {
#     "title": "Then Hunger Games",
#     "author": "Suzanne Collins",
#     "year": 2008,
#     "rating": 4.32,
#     "pages": 374
# }

# book2 = {
#     "title": "Hunger Games",
#     "author": "Suzanne Collins",
#     "year": 2009,
#     "rating": 4.12,
#     "pages": 300
# }

# book3 = {
#     "title": "After Hunger Games",
#     "author": "Suzanne Collins",
#     "year": 2011,
#     "rating": 4.1,
#     "pages": 354
# }

# def add_a_book():
#     print('Fill out the information to add your book.')
#     title = input("Title: ")
#     author = input("Author: ")
#     # year = int(input("Year published: "))
#     try:
#         year = int(input("Year published: "))
#     except:
#         year = int(input("Please enter a number for the year published: "))
#     # rating = float(input("Rating: "))
#     try:
#         rating = float(input("Rating: "))
#     except:
#         rating = float(input("Please enter a number for the rating: "))
#     # pages = int(input("# of pages: "))
#     try:
#         pages = int(input("# of pages: "))
#     except:
#         pages = int(input("Please enter a number for the number of pages: "))


#     book_dictionary = {
#       "title": title,
#       "author": author,
#       "year": year,
#       "rating": rating,
#       "pages": pages
#     }

#     return book_dictionary

# def book_details (book):
#     string = '' #"This is the book's info.\n"
#     for element in book:
#         if(element == 'title'):
#             # string = string + getTitle(book[element]) would run but wrote the get functions in next section so can't use in this one
#             string = string + f"The title is {book[element]}.\n"
#         elif(element == 'author'):
#             # string = string + getAuthor(book[element])
#             string = string + f"The author is {book[element]}.\n"
#         elif(element == 'year'):
#             # string = string + getYear(book[element])
#             string = string + f"The year published was {book[element]}.\n"
#         elif(element == 'rating'):
#             # string = string + getRating(book[element])
#             string = string + f"The book rating is {book[element]}.\n"
#         elif(element == 'pages'):
#             # string = string + getPages(book[element])
#             string = string + f"The number of pages in this book is {book[element]}."
#     return string

# def getBookByTitle(book_list, title):
#     for book in book_list:
#         if(book['title'] == title):
#             return book_details(book)
#     return 'Book not found'

# def getBookShelf(book_list):
#     shelf = ''
#     for num, book in enumerate(book_list):
#         shelf = shelf + f'Book {num+1}:\n' + book_details(book) + '\n'
#     return shelf

# book_list = [my_book, book2, book3]

# def main_menu():
#     print("What would you like to do with your bookshelf? 'Add a book', 'Select book by title', or 'Check bookshelf'")
#     result = input()

#     if result == 'Add a book':
#         book_list.append(add_a_book())
#         print('Successfully added your book')
#     elif result == 'Select book by title':
#         title = input("Enter title of book you'd like to search for: ")
#         print('\nResults:')
#         print(getBookByTitle(book_list=book_list, title=title))
#     elif result == 'Check bookshelf':
#         print('\nResults:')
#         print(getBookShelf(book_list=book_list))
    # pass
# main_menu()
### Step 5 - while loops

## Now add a while loop to your main menu to keep it alive, and continually asking for input until the user chooses to exit the program. Call the main menu to ensure it functions properly.

# Code here
my_book = {
    "title": "Then Hunger Games",
    "author": "Suzanne Collins",
    "year": 2008,
    "rating": 4.32,
    "pages": 374
}

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

def add_a_book():
    print('Fill out the information to add your book.')
    title = input("Title: ")
    author = input("Author: ")
    # year = int(input("Year published: "))
    try:
        year = int(input("Year published: "))
    except:
        year = int(input("Please enter a number for the year published: "))
    # rating = float(input("Rating: "))
    try:
        rating = float(input("Rating: "))
    except:
        rating = float(input("Please enter a number for the rating: "))
    # pages = int(input("# of pages: "))
    try:
        pages = int(input("# of pages: "))
    except:
        pages = int(input("Please enter a number for the number of pages: "))


    book_dictionary = {
      "title": title,
      "author": author,
      "year": year,
      "rating": rating,
      "pages": pages
    }

    return book_dictionary

def getTitle(title):
    return f"Title: {title}.\n"
def getAuthor(author):
    return f"Author: {author}.\n"
def getYear(year):
    return f"Year published: {year}.\n"
def getRating(rating):
    return f"Rating: {rating}.\n"
def getPages(pages):
    return f"# of pages: {pages}.\n"

def book_details (book):
    string = '' #"This is the book's info.\n"
    for element in book:
        if(element == 'title'):
            # string = string + getTitle(book[element]) would run but wrote the get functions in next section so can't use in this one
            # string = string + f"The title is {book[element]}.\n"
            string = string + getTitle(book[element])
        elif(element == 'author'):
            string = string + getAuthor(book[element])
            # string = string + f"The author is {book[element]}.\n"
        elif(element == 'year'):
            string = string + getYear(book[element])
            # string = string + f"The year published was {book[element]}.\n"
        elif(element == 'rating'):
            string = string + getRating(book[element])
            # string = string + f"The book rating is {book[element]}.\n"
        elif(element == 'pages'):
            string = string + getPages(book[element])
            # string = string + f"The number of pages in this book is {book[element]}."
    return string

def getBookByTitle(book_list, title):
    for book in book_list:
        if(book['title'] == title):
            return book_details(book)
    return 'Book not found'

def getBookShelf(book_list):
    shelf = ''
    for num, book in enumerate(book_list):
        shelf = shelf + f'Book {num+1}:\n' + book_details(book) + '\n'
    return shelf

book_list = [my_book, book2, book3]

def main_menu():
    run = True
    while(run):
        print("What would you like to do with your bookshelf? 'Add a book', 'Select book by title', or 'Check bookshelf'")
        print("Type 'exit' to stop the program")
        result = input()

        if result == 'Add a book':
            book_list.append(add_a_book())
            print('Successfully added your book')
        elif result == 'Select book by title':
            title = input("Enter title of book you'd like to search for: ")
            print('\nResults:')
            print(getBookByTitle(book_list=book_list, title=title))
        elif result == 'Check bookshelf':
            print('\nResults:')
            print(getBookShelf(book_list=book_list))
        elif result == 'exit':
            run = False
            print('Thank you for using the book library.')

main_menu()