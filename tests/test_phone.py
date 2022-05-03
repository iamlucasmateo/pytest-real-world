import pytest
from logic.business import Phonebook

# Fixture with finalizer (cleans up at the end in case it is needed)
@pytest.fixture
def my_book(request):
    # the file will be created and then destroyed with the finalizer
    with open("new_file.txt", "w") as f:
        f.write("some information")
    def clean_up():
        import os, time
        time.sleep(0.5)
        os.remove("new_file.txt")
    request.addfinalizer(clean_up)
    return Phonebook()

# tmpdir is a fixture provided by Pytest, automatically cleaned up after the tests are run
@pytest.fixture
def temp_data(tmpdir):
    with open(f"{tmpdir}/temp_book.txt", "w") as f:
        f.write("data")
    with open(f"{tmpdir}/temp_book.txt", "r") as f:
        return f.read()


def test_init_book(my_book):
    assert "entries" in my_book.__dict__
    assert my_book.__class__ == Phonebook

def test_add_name(my_book):
    my_book.add("Lucas", 1127865874)
    assert "Lucas" in my_book.entries
    assert my_book.entries["Lucas"] == 1127865874

# this fixture comes from the conftest.py file in this folder
def test_lookup(book_with_entries):
    assert book_with_entries.lookup("Pedro") == 1234

# this fixture comes from the conftest.py file in the parent folder
def test_names(other_book_with_entries):
    assert set(other_book_with_entries.names) == set({"Martina", "Juana"})

def test_temp(temp_data):
    assert temp_data == "data"
