import pytest
from logic.business import Phonebook

# conftest.py fixtures are available for all the tests in the folder

@pytest.fixture
def book_with_entries():
    book = Phonebook()
    book.add("Pedro", 1234)
    book.add("Juan", 5678)
    return book