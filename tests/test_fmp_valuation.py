import pytest

from fmp_py.fmp_valuation import FmpValuation
from fmp_py.models.valuation import CompanyRating


@pytest.fixture
def fmp_valuation():
    return FmpValuation()


def test_fmp_valuation_init(fmp_valuation):
    assert isinstance(fmp_valuation, FmpValuation)


def test_fmp_valuation_company_rating(fmp_valuation):
    valuation = fmp_valuation.company_rating("AAPL")
    assert isinstance(valuation, CompanyRating)
    assert valuation.symbol == "AAPL"
    assert isinstance(valuation.date, str)
    assert isinstance(valuation.rating, str)
    assert isinstance(valuation.rating_score, int)
    assert isinstance(valuation.rating_recommendation, str)
    assert isinstance(valuation.rating_details_dcf_score, int)
    assert isinstance(valuation.rating_details_dcf_recommendation, str)
    assert isinstance(valuation.rating_details_roe_score, int)
    assert isinstance(valuation.rating_details_roe_recommendation, str)
    assert isinstance(valuation.rating_details_roa_score, int)
    assert isinstance(valuation.rating_details_roa_recommendation, str)
    assert isinstance(valuation.rating_details_de_score, int)
    assert isinstance(valuation.rating_details_de_recommendation, str)
    assert isinstance(valuation.rating_details_pe_score, int)
    assert isinstance(valuation.rating_details_pe_recommendation, str)
    assert isinstance(valuation.rating_details_pb_score, int)
    assert isinstance(valuation.rating_details_pb_recommendation, str)


def test_fmp_valuation_company_rating_invalid_symbol(fmp_valuation):
    with pytest.raises(ValueError):
        fmp_valuation.company_rating("INVALID_SYMBOL")
