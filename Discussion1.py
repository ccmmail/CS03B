"""Example of class definition for CS03B Discussion 1."""

from dataclasses import dataclass, field

@dataclass
class Books(object):
    """Represent book object with ID, title, and number of pages.

    Getters raise an assertion error if argument is of incorrect type

    Args:
        ID: string unique alphanumeric ID
        title: string title of the book
        pages: integer number of pages in the book
    """
    ID: str = field(default = "0000")
    title: str = field(default = "Unknown")
    pages: int = field(default = 0)

    def __str__(self):
        """Return a string representation of self"""
        return f"{self.title} ({self.ID}), {self.pages} pages."

    def get_ID(self) -> str:
        return self.ID

    def get_title(self) -> str:
        return self.title

    def get_pages(self) -> int:
        return self.pages

    def set_ID(self, ID:str):
        try:
            assert type(ID) == str
        except AssertionError:
            print("Error: ID must be a string.")
        else:
            self.ID = ID

    def set_title(self, title:str):
        try:
            assert type(title) == str
        except AssertionError:
            print("Error: Title must be a string.")
        else:
            self.title = title

    def set_pages(self, pages:int):
        try:
            assert type(pages) == int
        except AssertionError:
            print("Error: Pages must be an integer.")
        else:
            self.pages = pages
