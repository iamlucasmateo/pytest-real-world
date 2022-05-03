import pytest
from logic.business import Phonebook

# conftest.py fixtures are available for all the tests in subfolders

@pytest.fixture
def other_book_with_entries():
    book = Phonebook()
    book.add("Martina", 123)
    book.add("Juana", 9876)
    return book