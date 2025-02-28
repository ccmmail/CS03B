"""Example of class definition for CS03B Discussion 1."""

from dataclasses import dataclass, field
import random

@dataclass
class Books(object):
    """Represent book object with ID, title, and number of pages.

    Setters raise an assertion error if argument is of incorrect type or
    if ID is not unique.

    Args:
        ID: string ID. Default random 10-digit numeric string.
            ValueException error upon init if ID is not unique.
        title: string title of the book.
        pages: integer number of pages in the book.
    """
    @staticmethod
    def _generate_ID() -> str:
        """Generate an ID for instantiating a book."""
        return(str(random.randint(1000000000, 9999999999)))

    ID: str = field(default_factory = _generate_ID)
    title: str = field(default = "Unknown")
    pages: int = field(default = 0)

    # Class level set to keep track of unique IDs
    _unique_IDs = set()

    def __post_init__(self):
        """Check that ID is unique on instantiation."""
        if self.ID in Books._unique_IDs:
            raise ValueError(f"ERROR: ID '{self.ID}' already exists.")
        else:
            Books._unique_IDs.add(self.ID)

    def __str__(self) -> str:
        """Return a string representation of self"""
        return f"{self.title} ({self.ID}), {self.pages} pages."

    def get_ID(self) -> str:
        return self.ID

    def get_title(self) -> str:
        return self.title

    def get_pages(self) -> int:
        return self.pages

    def set_ID(self, ID:str) -> None:
        try:
            assert type(ID) == str
        except AssertionError:
            print("ERROR: ID must be a string.")
        else:
            try:
                assert ID not in Books._unique_IDs
            except AssertionError:
                print("ERROR: ID must be unique.")
            else:
                Books._unique_IDs.remove(self.ID)
                self.ID = ID
                Books._unique_IDs.add(ID)

    def set_title(self, title:str) -> None:
        try:
            assert type(title) == str
        except AssertionError:
            print("ERROR: Title must be a string.")
        else:
            self.title = title

    def set_pages(self, pages:int) -> None:
        try:
            assert type(pages) == int
        except AssertionError:
            print("ERROR: Pages must be an integer.")
        else:
            self.pages = pages
