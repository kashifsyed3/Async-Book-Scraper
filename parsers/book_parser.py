from locators.book_locators import BookLocators
import re


class BookParser:

    RATINGS = {'One': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5}

    def __init__(self, book):
        self.book = book

    def __repr__(self):
        return f'<book: "{self.title}" - £{self.price} - {self.rating} stars - {self.is_in_stock}>'

    @property
    def title(self):
        locator = BookLocators.title
        title_tag = self.book.select_one(locator)
        return title_tag.attrs['title']

    @property
    def link(self):
        locator = BookLocators.link
        link_tag = self.book.select_one(locator)
        return link_tag.attrs['href']

    @property
    def rating(self):
        locator = BookLocators.rating
        price_tag = self.book.select_one(locator)
        rating_str = price_tag.attrs['class'][1]
        return BookParser.RATINGS.get(rating_str)

    @property
    def price(self):
        locator = BookLocators.price
        price_str = self.book.select_one(locator).string
        expression = '£([0-9]+\.[0-9]+)'
        return float(re.search(expression, price_str).group(1))

    @property
    def is_in_stock(self):
        locator = BookLocators.in_stock
        return self.book.select_one(locator).text.strip()
