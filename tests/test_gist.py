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