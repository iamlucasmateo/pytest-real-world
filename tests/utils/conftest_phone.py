from logic.business import Phonebook
import pytest

@pytest.fixture
def book_with_entries():
    book = Phonebook()
    book.add("Pedro", 1234)
    book.add("Juan", 5678)
    return book