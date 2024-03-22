### Step 1 - Store data in a .txt

## This step's instructions explains how to use the open() function, to write and read info from a .txt file. Follow the instructions to create and call a function to add a book, based off of the previous dictionaries for our library, to the .txt file properly formatted with commas as separators.

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

# def getTitle(title):
#     return f"Title: {title}.\n"
# def getAuthor(author):
#     return f"Author: {author}.\n"
# def getYear(year):
#     return f"Year published: {year}.\n"
# def getRating(rating):
#     return f"Rating: {rating}.\n"
# def getPages(pages):
#     return f"# of pages: {pages}.\n"

# def book_details (book):
#     string = '' #"This is the book's info.\n"
#     for element in book:
#         if(element == 'title'):
#             # string = string + getTitle(book[element]) would run but wrote the get functions in next section so can't use in this one
#             # string = string + f"The title is {book[element]}.\n"
#             string = string + getTitle(book[element])
#         elif(element == 'author'):
#             string = string + getAuthor(book[element])
#             # string = string + f"The author is {book[element]}.\n"
#         elif(element == 'year'):
#             string = string + getYear(book[element])
#             # string = string + f"The year published was {book[element]}.\n"
#         elif(element == 'rating'):
#             string = string + getRating(book[element])
#             # string = string + f"The book rating is {book[element]}.\n"
#         elif(element == 'pages'):
#             string = string + getPages(book[element])
#             # string = string + f"The number of pages in this book is {book[element]}."
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
#     run = True

#     book_list_created = False

#     while(run):
#         print("What would you like to do with your bookshelf? 'Add a book', 'Select book by title', or 'Check bookshelf'")
#         print("Type 'exit' to stop the program")
#         result = input()

#         if result == 'Add a book':
#             # book_list.append(add_a_book())
#             result = add_a_book()
#             if book_list_created == False:
#                 with open("library.txt", "w") as f:
#                     f.write(f"{result['title']}, {result['author']}, {result['year']}, {result['rating']}, {result['pages']}\n")
#                 book_list_created = True
#             else:
#                 with open("library.txt", "a") as f:
#                     f.write(f"{result['title']}, {result['author']}, {result['year']}, {result['rating']}, {result['pages']}\n")
#         elif result == 'Select book by title':
#             title = input("Enter title of book you'd like to search for: ")
#             print('\nResults:')
#             print(getBookByTitle(book_list=book_list, title=title))
#         elif result == 'Check bookshelf':
#             print('\nResults:')
#             print(getBookShelf(book_list=book_list))
#         elif result == 'exit':
#             run = False
#             print('Thank you for using the book library.')

# main_menu()

### Step 2 - Read data from a .txt

## Now take your previously create function which prints info about all the books in your library, but gets the info from a list, and make it work by reading the information in your home library's .txt document. This will take some new logic, but you can do it.

# Code here
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

# def getTitle(title):
#     return f"Title: {title}\n"
# def getAuthor(author):
#     return f"Author: {author}\n"
# def getYear(year):
#     return f"Year published: {year}\n"
# def getRating(rating):
#     return f"Rating: {rating}\n"
# def getPages(pages):
#     return f"# of pages: {pages}\n"

# def book_details (book):
#     string = '' #"This is the book's info.\n"
#     for element in book:
#         if(element == 'title'):
#             # string = string + getTitle(book[element]) would run but wrote the get functions in next section so can't use in this one
#             # string = string + f"The title is {book[element]}.\n"
#             string = string + getTitle(book[element])
#         elif(element == 'author'):
#             string = string + getAuthor(book[element])
#             # string = string + f"The author is {book[element]}.\n"
#         elif(element == 'year'):
#             string = string + getYear(book[element])
#             # string = string + f"The year published was {book[element]}.\n"
#         elif(element == 'rating'):
#             string = string + getRating(book[element])
#             # string = string + f"The book rating is {book[element]}.\n"
#         elif(element == 'pages'):
#             string = string + getPages(book[element])
#             # string = string + f"The number of pages in this book is {book[element]}."
#     return string

# def getBookByTitle(book_list, title):
#     for book in book_list:
#         if(book['title'] == title):
#             return book_details(book)
#     return 'Book not found'

# def getBookShelf(book_list):
#     shelf = ''
#     # for num, book in enumerate(book_list):
#     #     shelf = shelf + f'Book {num+1}:\n' + book_details(book) + '\n'
#     num = 1 # tracks book number in library
#     with open("library.txt", "r") as f:
#         file = f.readlines()

#         for line in file:
            
#             line = line.split(", ")

#             book_dictionary = {
#                 "title": line[0],
#                 "author": line[1],
#                 "year": line[2],
#                 "rating": line[3],
#                 "pages": line[4]
#             }
#             shelf = shelf + f'Book {num}:\n' + book_details(book_dictionary)
#             num += 1
#     return shelf

# def main_menu():
#     run = True

#     book_list_created = False

#     while(run):
#         print("What would you like to do with your bookshelf? 'Add a book', 'Select book by title', or 'Check bookshelf'")
#         print("Type 'exit' to stop the program")
#         result = input()

#         if result == 'Add a book':
#             # book_list.append(add_a_book())
#             result = add_a_book()
#             if book_list_created == False:
#                 with open("library.txt", "w") as f:
#                     f.write(f"{result['title']}, {result['author']}, {result['year']}, {result['rating']}, {result['pages']}\n")
#                 book_list_created = True
#             else:
#                 with open("library.txt", "a") as f:
#                     f.write(f"{result['title']}, {result['author']}, {result['year']}, {result['rating']}, {result['pages']}\n")
#         elif result == 'Select book by title':
#             title = input("Enter title of book you'd like to search for: ")
#             print('\nResults:')
#             print(getBookByTitle(book_list=book_list, title=title))
#         elif result == 'Check bookshelf':
#             print('\nResults:')
#             print(getBookShelf(book_list=book_list))
#         elif result == 'exit':
#             run = False
#             print('Thank you for using the book library.')

# main_menu()

### Step 3 - if __name__ == "__main__":

## Wrap your main menu function call in an "if __name__ == '__main__':" statement to ensure it doesn't accidentally run if this file is imported as a module elsewhere.

# Code this at the bottom of the script
# if __name__ == "__main__":
#     main_menu()

### Step 4 - Expand and refactor

## Now follow the instructions in this final step. Expand your project. Clean up the code. Make your application functional. Great job getting your first Python application finished!

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
    return f"Title: {title}\n"
def getAuthor(author):
    return f"Author: {author}\n"
def getYear(year):
    return f"Year published: {year}\n"
def getRating(rating):
    return f"Rating: {rating}\n"
def getPages(pages):
    return f"# of pages: {pages}\n"

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

def getBookShelf():
    shelf = ''

    num = 1 # tracks book number in library
    with open("library.txt", "r") as f:
        file = f.readlines()

        for line in file:
            
            line = line.split(", ")

            book_dictionary = {
                "title": line[0],
                "author": line[1],
                "year": line[2],
                "rating": line[3],
                "pages": line[4]
            }
            shelf = shelf + f'Book {num}:\n' + book_details(book_dictionary)
            num += 1
    return shelf

def getBookByTitle(title):
    with open("library.txt", "r") as f:
        file = f.readlines()

        for line in file:
            
            line = line.split(", ")

            book_dictionary = {
                "title": line[0],
                "author": line[1],
                "year": line[2],
                "rating": line[3],
                "pages": line[4]
            }
            if(book_dictionary['title'] == title):
                return book_details(book_dictionary)
    return 'Book not found'

def getBookByAuthor(author):
    shelf = ''

    num = 1 # tracks book number in library
    with open("library.txt", "r") as f:
        file = f.readlines()

        for line in file:
            
            line = line.split(", ")

            book_dictionary = {
                "title": line[0],
                "author": line[1],
                "year": line[2],
                "rating": line[3],
                "pages": line[4]
            }
            if(book_dictionary['author'] == author):
                shelf = shelf + f'Book {num}:\n' + book_details(book_dictionary)
                num += 1
    if len(shelf) > 0:
        return shelf
    else:
        return 'No books written by that author exist in this library'

def getAverageRating():
    rating = 0
    num = 0
    with open("library.txt", "r") as f:
        file = f.readlines()

        for line in file:
            
            line = line.split(", ")

            book_dictionary = {
                "title": line[0],
                "author": line[1],
                "year": line[2],
                "rating": line[3],
                "pages": line[4]
            }
            rating += float(book_dictionary["rating"])
            num += 1
    return str(rating / num)

def main_menu():
    run = True

    book_list_created = False

    while(run):
        print("What would you like to do with your bookshelf? 'Add a book', 'Select book by title', 'Select book by author', 'Average rating of bookshelf' or 'Check bookshelf'")
        print("Type 'exit' to stop the program")
        result = input()

        if result == 'Add a book':
            result = add_a_book()
            if book_list_created == False:
                with open("library.txt", "w") as f:
                    f.write(f"{result['title']}, {result['author']}, {result['year']}, {result['rating']}, {result['pages']}\n")
                book_list_created = True
            else:
                with open("library.txt", "a") as f:
                    f.write(f"{result['title']}, {result['author']}, {result['year']}, {result['rating']}, {result['pages']}\n")
        elif result == 'Select book by title':
            title = input("Enter title of the book you'd like to search for: ")
            print('\nResults:')
            print(getBookByTitle(title=title))
        elif result == 'Select book by author':
            author = input("Enter the author of the book(s) you'd like to search for: ")
            print('\nResults:')
            print(getBookByAuthor(author=author))
        elif result == 'Average rating of bookshelf':
            print('\nResult:')
            print(getAverageRating() + '\n')
        elif result == 'Check bookshelf':
            print('\nResults:')
            print(getBookShelf())
        elif result == 'exit':
            run = False
            print('Thank you for using the book library.')

if __name__ == "__main__":
    main_menu()