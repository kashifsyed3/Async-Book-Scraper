from locators.page_locators import PageLocators
from parsers.book_parser import BookParser, re
from bs4 import BeautifulSoup


class PageParser:

    def __init__(self, page):
        self.soup = BeautifulSoup(page, 'html.parser')

    @property
    def books(self):
        locator = PageLocators.books
        books = self.soup.select(locator)
        return [BookParser(book) for book in books]

    @property
    def total_pages(self):
        locator = PageLocators.pager
        pager_str = self.soup.select_one(locator).string
        expression = 'Page ([0-9]+) of ([0-9]+)'
        return int(re.search(expression, pager_str).group(2))
