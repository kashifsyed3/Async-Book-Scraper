import logging
from app import books

logger = logging.getLogger('book_scraper')

user_choice = """Enter one of the following:
 - 'f' to look at 5 star books
 - 'c' to look at 5 cheapest books
 - 'n' to look at the next book in catalogue
 - 'q' to quit
 -->"""


def best_books():
    for book in books:
        if book.rating == 5:
            print(book)


def cheapest_books():
    for book in (sorted(books, key=lambda x: x.price)[:5]):
        print(book)


g = (book for book in books)


def next_book():
    print(next(g))
    print(next(g))


def menu():
    user_input = input(user_choice)

    while user_input != 'q':

        if user_input == 'f':
            best_books()

        elif user_input == 'c':
            cheapest_books()

        elif user_input == 'n':
            next_book()

        else:
            print("Invalid option entered")

        user_input = input(user_choice)


menu()

logger.info('Terminating program')