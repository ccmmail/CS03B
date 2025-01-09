"""Example of class definition for CS03B Discussion 1."""

from dataclasses import dataclass, field

@dataclass
class Books(object):
    """Represent book object with ID, title, and number of pages.

    Getters raise an assertion error if argument is of incorrect type

    Args:
        ID: string ID. ValueException error if ID is not unique
        title: string title of the book
        pages: integer number of pages in the book
    """
    ID: str = field(default = "0000")
    title: str = field(default = "Unknown")
    pages: int = field(default = 0)

    # Class level set to keep track of unique IDs
    _unique_IDs = set()

    def __post_init__(self):
        """Check that ID is unique on instantiation."""
        if self.ID in Books._unique_IDs and self.ID != "0000":
            raise ValueError(f"ERROR: ID '{self.ID}' already exists.")
        else:
            Books._unique_IDs.add(self.ID)

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
            print("ERROR: ID must be a string.")
        else:
            try:
                assert ID not in Books._unique_IDs
            except AssertionError:
                print("ERROR: ID must be unique.")
            else:
            #   if ID in self._unique_IDs:
            #        self._unique_IDs.remove(self.ID)
                Books._unique_IDs.remove(self.ID)
                self.ID = ID
                Books._unique_IDs.add(ID)

    def set_title(self, title:str):
        try:
            assert type(title) == str
        except AssertionError:
            print("ERROR: Title must be a string.")
        else:
            self.title = title

    def set_pages(self, pages:int):
        try:
            assert type(pages) == int
        except AssertionError:
            print("ERROR: Pages must be an integer.")
        else:
            self.pages = pages

