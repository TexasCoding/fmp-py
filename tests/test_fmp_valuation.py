import pytest

from fmp_py.fmp_valuation import FmpValuation


@pytest.fixture
def fmp_valuation():
    return FmpValuation()


def test_fmp_valuation_init(fmp_valuation):
    assert isinstance(fmp_valuation, FmpValuation)
