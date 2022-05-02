import pytest

def test_first_test():
    assert 1 == 1

# mark and skip
@pytest.mark.skip
def test_should_be_skipped():
    assert 1 == 2


# conditional skip
@pytest.mark.skipif(True, reason="Skipped because reason")
def test_skip_conditional():
    assert 1 == 2


# for flaky tests
@pytest.mark.xfail
def test_xfail():
    assert 1 == 2

# custom marks 
@pytest.mark.slow
def test_slow():
    assert 1 == 1

class Company:
    def __init__(self, name: str, stock_symbol: str):
        self.name = name
        self.stock_symbol = stock_symbol
    
    def __str__(self):
        return f"{self.name}:{self.stock_symbol}"

# Fixtures
@pytest.fixture
def company() -> Company:
    return Company(name="Fiver", stock_symbol="FVRR")

# the company parameter will be taken from the fixtures
def test_with_fixture(company):
    print(f"Printing {company} from fixture")


# Parametrize
@pytest.mark.parametrize(
    "company_name",   
    ["TikTok", "Instagram", "Discord"],
    ids=["TIKTOK_TEST", "INSTAGRAM_TEST", "DISCORD_TEST"]
)
def test_with_parameters(company_name): # argument from parameter
    print(f"Parameter: {Company(company_name, 'XXX')}")


# Testing exceptions
def raise_exc(): 
    raise ValueError("This is an exception")

def test_raise_exepction():
    with pytest.raises(ValueError) as e:
        raise_exc()
    assert "This is an exception" == str(e.value)
