import pytest
from typing import List
from unittest.mock import MagicMock, patch

from logic.business import Company, useful

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

# Fixtures: they are created (and destroyed) before each function that needs it
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


# Fixtures with arguments
@pytest.fixture
def company_factory(**kwargs):
    def _company_factory(**kwargs) -> Company:
        company_name = kwargs.pop("name", "Test Company")
        company_stock_symbol = kwargs.pop("stock", "TEST")
        return Company(company_name, company_stock_symbol)
    return _company_factory

def test_3_cases(company_factory):
    google = company_factory(name="google", stock="GOOG")
    yahoo = company_factory(name="yahoo", stock="YAHOO")
    test = company_factory()
    assert google.name == "google"
    assert yahoo.stock_symbol == "YAHOO"
    assert test.name == "Test Company"

# Indirect parameterization

@pytest.fixture
# uses company fixture
def companies(request, company) -> List[Company]:
    companies = []
    names = request.param
    for name in names:
        companies.append(Company(name=name))
    
    return companies

@pytest.mark.parametrize(
    "companies", 
    [["google", "yahoo"], ["facebook", "instagram"]], 
    indirect=True
)
def test_companies(companies):
    company_names = set([x.name for x in companies])
    expected_names_0 = set(["google", "yahoo"])
    expected_names_1 = set(["facebook", "instagram"])
    if "google" in company_names:
        assert company_names == expected_names_0
    if "facebook" in company_names:
        assert company_names == expected_names_1

# mocking: use the path from which the function is used, not the one in which it is defined
# db_utils is defined in the utils module, but we use it in the business module
@patch("logic.business.db_utils", MagicMock(return_value=42))
def test_mocking_utils():
    assert useful() == 42

def test_mocking_utils_other_syntax():
    with patch("logic.business.db_utils", MagicMock(return_value=42)) as mock_db_write:
        assert useful() == 42