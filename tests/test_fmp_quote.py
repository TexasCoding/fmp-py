import pytest

from fmp_py.fmp_quote import FmpQuote


@pytest.fixture
def fmp_quote():
    return FmpQuote()


def test_fmp_quote_init(fmp_quote):
    assert isinstance(fmp_quote, FmpQuote)
