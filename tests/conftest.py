import pytest
from logic.business import Phonebook

# conftest.py fixtures are available for all the tests in the folder
# they can be imported from another file
from tests.utils.conftest_phone import book_with_entries

# or import them as plugins
# pytest_plugins = [
#     "tests.utils.conftest_phone"
# ]

@pytest.fixture
def book_with_entries_other():
    book = Phonebook()
    book.add("Martina", 1234)
    book.add("Lucas", 5678)
    return book